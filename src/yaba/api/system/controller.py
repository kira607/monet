import hashlib
import hmac
from typing import Any, Dict, Tuple, Union

import git
from flask import current_app


class SystemController:
    """A controller for internal requests (web hooks, server health, etc.)."""

    def __init__(self) -> None:
        self._deploy_secret_key = current_app.config.get("DEPLOY_SECRET_KEY")

    def deploy_web_hook(
        self, x_hub_signature: str, data: bytes
    ) -> Tuple[Union[Dict[Any, Any], str], int]:
        """
        Process a web hook from github.

        This web hook is triggered when a project repo
        is updated (push). Triggering it will
        tell pythonanywhere.com to pull a repo
        and reload a web application.

        :param x_hub_signature: A signature from github.
        :param data: A web hook data to validate a request.
        """
        if self._deploy_secret_key is None:
            return {
                "error": "Update server: failed. Secret token is not configured"
            }, 500

        if not self._is_valid_signature(x_hub_signature, data):
            return "Invalid token, deploy aborted.", 403

        repo = git.Repo(".")
        origin = repo.remotes.origin
        origin.pull()

        return "Update server: success", 200

    def _is_valid_signature(self, x_hub_signature: str, data: bytes) -> bool:
        private_key = self._deploy_secret_key
        hash_algorithm, github_signature = x_hub_signature.split("=", 1)
        algorithm = hashlib.__dict__.get(hash_algorithm)
        encoded_key = bytes(private_key, "latin-1")  # type: ignore
        mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)  # type: ignore
        return hmac.compare_digest(mac.hexdigest(), github_signature)
