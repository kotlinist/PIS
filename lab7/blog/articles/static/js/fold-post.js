const buttons = document.querySelectorAll(".fold-button");
console.log("Buttons found:");
console.log(buttons);

Array.from(buttons).forEach((button) => {
  button.addEventListener("click", function (e) {
    console.log("Кнопка нажата!");
    console.log("you clicked ", e.target);
    // Получаем родительский элемент поста (элемент с классом one-post)
    var postElement = e.target.parentElement.parentElement;

    // Проверяем, есть ли у родителя класс folded
    if (postElement.className.indexOf("folded") !== -1) {
      // Если пост свернут - разворачиваем
      postElement.className = postElement.className.replace("folded", "");
      e.target.innerHTML = "свернуть";
    } else {
      // Если пост развернут - сворачиваем
      postElement.className = postElement.className + " folded";
      e.target.innerHTML = "развернуть";
    }
  });
});
