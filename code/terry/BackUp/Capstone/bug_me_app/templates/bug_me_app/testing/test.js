// function textInsert() {
//     let x = document.getElementById('titleText');
//     let y = document.getElementById('bodyText');
//     x.setAttribute('value', 'title_text_from_array');
//     document.getElementById('bodyText').innerText = body_text_from_array;
//     document.body.appendChild(x);
// }

// function createLink() {
//     let result = 'id_from_the_link_clicked';
//     this.textInsert();
// }

// addTask: function() {
//         let inputTask = item.body
//         if (inputTask.trim()) {
//             let objTask = {
//                 name: inputTask,
//                 state: true
//             }
//             this.tasks.unshift(objTask)
//         }
//     },



//     // ************************ Drag and drop ***************** //
//     let dropArea = document.getElementById("drop-area")

// // Prevent default drag behaviors
// ;
// ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
//     dropArea.addEventListener(eventName, preventDefaults, false)
//     document.body.addEventListener(eventName, preventDefaults, false)
// })

// // Highlight drop area when item is dragged over it
// ;
// ['dragenter', 'dragover'].forEach(eventName => {
//     dropArea.addEventListener(eventName, highlight, false)
// })

// ;
// ['dragleave', 'drop'].forEach(eventName => {
//     dropArea.addEventListener(eventName, unhighlight, false)
// })

// // Handle dropped files
// dropArea.addEventListener('drop', handleDrop, false)

// function preventDefaults(e) {
//     e.preventDefault()
//     e.stopPropagation()
// }

// function highlight(e) {
//     dropArea.classList.add('highlight')
// }

// function unhighlight(e) {
//     dropArea.classList.remove('active')
// }

// function handleDrop(e) {
//     var dt = e.dataTransfer
//     var files = dt.files

//     handleFiles(files)
// }

// let uploadProgress = []
// let progressBar = document.getElementById('progress-bar')

// function initializeProgress(numFiles) {
//     progressBar.value = 0
//     uploadProgress = []

//     for (let i = numFiles; i > 0; i--) {
//         uploadProgress.push(0)
//     }
// }

// function updateProgress(fileNumber, percent) {
//     uploadProgress[fileNumber] = percent
//     let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length
//     console.debug('update', fileNumber, percent, total)
//     progressBar.value = total
// }

// function handleFiles(files) {
//     files = [...files]
//     initializeProgress(files.length)
//     files.forEach(uploadFile)
//     files.forEach(previewFile)
// }

// function previewFile(file) {
//     let reader = new FileReader()
//     reader.readAsDataURL(file)

//     reader.onloadend = function() {
//         let img = document.createElement('img')
//         img.src = reader.result
//         console.log(img)
//         document.getElementById('gallery').appendChild(img)
//     }
// }

// function uploadFile(file, i) {
//     var url = 'https://api.cloudinary.com/v1_1/denwboz1f/image/upload/'
//     var xhr = new XMLHttpRequest()
//     var formData = new FormData()
//     xhr.open('POST', url, true)
//     xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')

//     // Update progress (can be used to show progress indicator)
//     xhr.upload.addEventListener("progress", function(e) {
//         updateProgress(i, (e.loaded * 100.0 / e.total) || 100)
//     })

//     xhr.addEventListener('readystatechange', function(e) {
//         if (xhr.readyState == 4 && xhr.status == 200) {
//             updateProgress(i, 100) // <- Add this
//         } else if (xhr.readyState == 4 && xhr.status != 200) {
//             // Error. Inform the user
//         }
//     })

//     formData.append('upload_preset', 'o612psyj')
//     formData.append('file', file)
//     xhr.send(formData)
// }

let url = 'process.php'
let form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    let files = document.querySelector('[type=file]').files
    let formData = new FormData()

    for (let i = 0; i < files.length; i++) {
        let file = files[i]

        formData.append('files[]', file)
    }

    fetch(url, {
        method: 'POST',
        body: formData,
    }).then(response => {
        console.log(response)
    })
})