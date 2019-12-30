let Conan = { Name: "Conan", Location: "Cimmeria", Era: "Hyperborian", Conquest: "Aquilonia" };
let Rommel = { Name: "Rommel", Location: "Germany", Era: "WW2", Conquest: "Northern Africa" };

let hero = [Conan, Rommel];
hero2 = JSON.parse(localStorage.getItem('hero'));

let createForm = document.createElement('form'); // Create New Element Form
let ul = document.getElementById('target-ul');

function search(hero, query) {
    for (i=0; i<hero.length; i++) {
        if (hero[i].Name === query) {
            return hero[i];
        }
    }
    console.log("Not Found")
}

let liMaker = text => {     //list maker function
    let li = document.createElement('li');
    output = '';
    for (key in text) {
        output += key;
        output += ': ';
        output += text[key];
        output += '\n';
        };
    li.innerText = output;
    ul.append(li);
    };

function lineBreak() {
    let line = document.createElement('hr'); // Giving Horizontal Row After Heading
    createForm.appendChild(line);

    let linebreak = document.createElement('br');
    createForm.appendChild(linebreak);
};
//Hides the Edit and Delete buttons initially
document.getElementById('edit').style.display = "none";
document.getElementById('del').style.display = "none";
document.getElementById('edit-form').style.display = "none";
document.getElementById('searchbtn').style.display = "none";


let newPost = document.getElementById("new-hero");
let submit = document.getElementById("submit");

let target = document.getElementById("target");
let deleteSelectedButton = document.getElementById("del");

submit.addEventListener('click', function(event) {  //"add a hero" button
    event.preventDefault();     //stops the page from resubmitting the page
    
    submit.style.display = "none";
    let x = document.getElementById("hero-form");
    createForm.setAttribute("action", ""); // Setting Action Attribute on Form
    createForm.setAttribute("method", "post"); // Setting Method Attribute on Form
    x.appendChild(createForm);

    let heading = document.createElement('h2'); // Heading of Form
    heading.innerHTML = "Add a hero";
    createForm.appendChild(heading);

    let namelabel = document.createElement('label'); // Create Label for Name Field
    namelabel.innerHTML = "Name: "; // Set Field Labels
    createForm.appendChild(namelabel);

    let nameElement = document.createElement('input'); // Create Input Field for Name
    nameElement.setAttribute("type", "text");
    nameElement.setAttribute("name", "dname");
    createForm.appendChild(nameElement);

    lineBreak()

    locLabel = document.createElement('label'); // Create Label for Location Field
    locLabel.innerHTML = "Location: ";
    createForm.appendChild(locLabel);

    let locElement = document.createElement('input'); // Create Input Field for Location
    locElement.setAttribute("type", "text");
    locElement.setAttribute("name", "dlocation");
    createForm.appendChild(locElement);

    lineBreak()

    eraLabel = document.createElement('label'); // Create Label for Era Field
    eraLabel.innerHTML = "Era: ";
    createForm.appendChild(eraLabel);

    let eraElement = document.createElement('input'); // Create Input Field for Era
    eraElement.setAttribute("type", "text");
    eraElement.setAttribute("name", "dera");
    createForm.appendChild(eraElement);

    lineBreak()

    conLabel = document.createElement('label'); // Create Label for Conquest Field
    conLabel.innerHTML = "Conquest: ";
    createForm.appendChild(conLabel);

    let conElement = document.createElement('input'); // Create Input Field for Conquest
    conElement.setAttribute("type", "text");
    conElement.setAttribute("name", "dconquest");
    createForm.appendChild(conElement);

    lineBreak()

    let saveButton = document.createElement("button"); // Append Submit Button
    saveButton.innerText = "ADD";
    saveButton.setAttribute("type", "submit");
    // saveButton.setAttribute("name", "dsubmit");
    // saveButton.setAttribute("value", "Submit");
    saveButton.addEventListener('click', function(event) {
        event.preventDefault();
        console.log(submit);
        submit.style.display = "inline";
        console.log(submit);
        let actionList = { Name: nameElement.value, Location: locElement.value, Era: eraElement.value, Conquest: conElement.value };
        hero.push(actionList);
        localStorage.setItem('hero', JSON.stringify(hero))
        // localStorage.setItem('Name', nameElement.value);
        // localStorage.setItem('Era', eraElement.value);
        // localStorage.setItem('Location', locElement.value);
        // localStorage.setItem('Conquest', conElement.value);
        createForm.style.display = "none";    
    });
    createForm.appendChild(saveButton);
    
});

assemble.addEventListener('click', function(event) {    //"See all entered heroes" button
    event.preventDefault();     //stops the page from resubmitting the page
    savedHeroes = JSON.parse(localStorage.getItem('hero'));
    console.log(savedHeroes);

    let retrieve = document.createElement('retrieve');
    retrieve.textContent = savedHeroes;
    
    //liMaker(savedHeroes)

    createForm.setAttribute("action", ""); // Setting Action Attribute on Form
    createForm.setAttribute("method", "post"); // Setting Method Attribute on Form
    retrieve.appendChild(createForm);
    console.log(savedHeroes)
    savedHeroes.forEach(hero => {
        liMaker(hero)
      });

    document.getElementById('edit').style.display = "inline";
    document.getElementById('del').style.display = "inline";

    edit.addEventListener('click', function(event) {
        event.preventDefault();
        document.getElementById('edit-form').style.display = "inline";
        document.getElementById('edit').style.display = "none";
        document.getElementById('del').style.display = "none";
    
        let x = document.getElementById("edit-form");
        createForm.setAttribute("action", ""); // Setting Action Attribute on Form
        createForm.setAttribute("method", "post"); // Setting Method Attribute on Form
        x.appendChild(createForm);

        let nameElement = document.createElement('input'); // Create Input Field to search for Names
        nameElement.setAttribute("type", "text");
        nameElement.setAttribute("name", "dname");
        createForm.appendChild(nameElement);

        if (nameElement in hero) {
            document.getElementById('edit-form').innerHTML = search(nameElement);

            }

        document.getElementById('searchbtn').style.display = "inline";    
        searchbtn.addEventListener('click', function(event) {
            event.preventDefault();
        
            let fields = document.createElement('input'); // Create Input Field to search for fields
            fields.setAttribute("type", "text");
            fields.setAttribute("name", "dname");
            createForm.appendChild(fields);
            console.log(nameElement.value)
            console.log(hero)
            document.getElementById('edit-form').innerHTML = search(nameElement.value);

        });
            
});

    del.addEventListener('click', function(event) {     //clears localStorage, deleting ALL heroes
        event.preventDefault();
        // let li = savedHeroes.Name;
        localStorage.clear()
        while (ul.firstChild) {
          ul.removeChild(ul.firstChild)
        };
    });    

});

localStorage.setItem('hero', JSON.stringify(hero))