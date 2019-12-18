let Conan = {Name: "Conan", Location: "Cimmeria", Era: "Hyperborian", Conquest: "Aquilonia"};
let Rommel = {Name: "Rommel", Location: "Germany", Era: "WW2", Conquest: "Northern Africa"};

let hero = [Conan, Rommel];
hero2 = JSON.parse(localStorage.getItem('hero'));
console.log(hero2)
// Is an empty entry necessary based on the create function below?
let General = {Name: "", Location: "", Era: "", Conquest: ""};


//Great little function in JS called 'find.' Look into it.
function search(hero, query) {
    for (i=0; i<hero.length; i++) {
        if (hero[i].Name === query) {
            return hero[i];
        }
    }
    console.log("Not Found")
}

lions = true;
while (lions === true) {
    console.log("Hello! Today we're working with a list of historical generals.");
    let action = prompt("You can create, retrieve, update, or delete a record.");

    if (action.includes('c')) {
        let name = prompt("Name: ");
        let location = prompt("Location: ");
        let era = prompt("Era: ");
        let conquest = prompt("Conquest: ");
        let actionList = {Name: name, Location: location, Era: era, Conquest: conquest};
        hero.push(actionList);
    }
    else if (action.includes('r')) {
        let info = prompt("Whose information would you like to see?");
        console.log(search(hero, info));
    }
    else if (action.includes('u')) {
        let info = prompt("Whose information would you like to update?");
        let newValue = search(hero, info);
        let field = prompt("Which field would you like to update?")
        if (newValue.hasOwnProperty(field)) {
            newValue[field] = prompt("Enter you update: ")
        }

    }
    else if (action.includes('d')) {
        let info = prompt("Whose information would you like to delete?");
        let delValue = hero.indexOf(search(hero, info));    //gets the index value of the hero you're searching for
        let confirm = prompt("Enter \'d\' to delete this entry: ");
        if (confirm === 'd'){
            hero.splice(delValue, 1);
        } else {
            continue;
        }
        console.log(hero)
    }
    else if(action.includes('q')){
        break
    }
}

console.log(hero)
localStorage.setItem('hero', JSON.stringify(hero))