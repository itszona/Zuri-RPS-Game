firstNumber = prompt("Enter first number: ");
firstNumber = Number(firstNumber)

secondNumber = prompt("Enter second number: ");
secondNumber = Number(secondNumber)

operation = prompt("Pick one of the folloeing operations: +-*/");
if (operation == '+'){
    result = firstNumber + secondNumber;
    alert(result);
}
else if (operation == '-'){
    result = firstNumber - secondNumber;
    alert(result);
}

else if (operation == '*'){
    result = firstNumber * secondNumber;
    alert(result);
}

else if (operation == '/'){
    result = firstNumber / secondNumber;
    alert(result);
}

else {
    alert("That is not a valid operation!")
}
