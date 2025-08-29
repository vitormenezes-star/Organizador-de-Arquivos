const display = document.getElementById("display");

function addChar(char) {
  display.value += char;
}

function clearDisplay() {
  display.value = "";
}

function delChar() {
  display.value = display.value.slice(0, -1);
}

function calculate() {
  try {
    display.value = eval(display.value);
  } catch {
    display.value = "Erro";
    setTimeout(() => display.value = "", 1000);
  }
}
