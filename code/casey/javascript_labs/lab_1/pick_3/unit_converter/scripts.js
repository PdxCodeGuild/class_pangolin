let input = document.getElementById("input");
let btn = document.getElementById("btn");
let answer = document.getElementById("answer");

function convert() {
    let x = input.value;
    let y = x * 0.3048;
    answer.innerText = `Great! ${x} feet is ${y} meters.`;
}

btn.addEventListener("click", function(e) {
    console.log("done")
    convert();
    console.log("finished")
    input.value = "";
    console.log("cooked")
});


// //  user greeting
// print("\nGreetings!\nThis is a simple distance unit converter.")

// //  define user input
// x = float(input("Type a number of feet to receive the equivalent in meters: "))

// //  convert
// y = x * 0.3048

// //  return user's conversion
// print(f"\nGreat! {x} feet is {y} meters.")

// //  end program
// print("Thanks for using this simple distance unit converter!\nGoodbye.")