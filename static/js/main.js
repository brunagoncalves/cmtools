// Rich Text
var quill = new Quill("#editor", {
  modules: {
    toolbar: [
      [{ header: [1, 2, false] }],
      ["bold", "italic", "underline"],
      ["image", "code-block"],
    ],
  },
  placeholder: "Compose an epic...",
  theme: "snow", // or 'bubble'
});

document.querySelector("form").onsubmit = function () {
  var content = document.querySelector("input[name=content]");
  content.value = quill.root.innerHTML;
};// 3 segundos (3000 milissegundos)
