 function showModal(titleHtml, contentHtml, buttons) {
  const modal = document.createElement("div");

  modal.classList.add("modal");
  modal.innerHTML = `
        <div class="modal__inner">
            <div class="modal__top">
                <div class="modal__title">${titleHtml}</div>
                <button class="modal__close" type="button">
                    <span class="material-icons">close</span>
                </button>
            </div>
            <div class="modal__content">${contentHtml}</div>
            <div class="modal__bottom"></div>
        </div>
    `;

  for (const button of buttons) {
    const element = document.createElement("button");

    element.setAttribute("type", "button");
    element.classList.add("modal__button");
    element.textContent = button.label;
    element.addEventListener("click", () => {
      if (button.triggerClose) {
        document.body.removeChild(modal);
      }

      button.onClick(modal);
    });

    modal.querySelector(".modal__bottom").appendChild(element);
  }

  modal.querySelector(".modal__close").addEventListener("click", () => {
    document.body.removeChild(modal);
  });

  document.body.appendChild(modal);
}

showModal("Sample Modal Title", "<p>I am the content of this modal</p>", [
  {
    label: "Got it!",
    onClick: (modal) => {
      console.log("The button was clicked!");
    },
    triggerClose: false
  },
  {
    label: "Decline",
    onClick: (modal) => {
      console.log("DECLINED.");
    },
    triggerClose: false
  }
]);
