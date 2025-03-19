function sendrequest() {
  document.getElementById('my_button').addEventListener('click', function() {
    fetch('hi')
      .then(response => {
        console.log('Raw Response:', response); // Log the entire Response object
        return response.text(); // Continue to get the body text
      })
      .then(text => {
        console.log('Response Body Text:', text); // Log the body content
      });
  });
}
function createButton(response){
  let container=document.getElementById('button_container');
  for (let i = 0; i < response.length; i++) {
    namee=response[i];
    const button=document.createElement('button')
    button.textContent=namee;
    button.id= `file-${namee}`;
    button.addEventListener('click',function(){
    const buttonName = button.textContent; // Get the button’s name
    //console.log(buttonName);              // Log it (or return it)
    drawFolders(buttonName,false);
    })
    //console.log(response[i]);
    container.appendChild(button);
  }
}
function drawFolders(folder_pressed,initial){  
  //console.log(folder_pressed)                  //use the value of the span element which stores value for current directory
  const spanElement = document.getElementById('current_dir');
  const currentDir = spanElement.textContent;
  
 
  if (initial){
    fetch(`/files?dir=${encodeURIComponent(currentDir)}`)
    .then(function(response){
      return response.json();
    })
    .then (function(response){
      createButton(response);
    })

  }
  else{
    let container=document.getElementById('button_container');
    const element=document.getElementById('current_dir');
    container.innerHTML='';
    new_path=encodeURIComponent(currentDir+'\\'+folder_pressed);
      //console.log(new_path);
  fetch(`/files?dir=${new_path}`)
  .then(function(response){
    return response.json();

  }).then (function(response){
    createButton(response);
  })
  
  element.textContent= element.textContent+'\\'+folder_pressed;


}
}
function goBack() {
  const element=document.getElementById('current_dir');
  fetch(`/files?command=back`)
    .then(function(response) {
      return response.text();
    })
    .then(function(response) {
      console.log(response)
      
      createButton(response)
    }); // Close second .then
} // Close function

function initialize(){
  const element=document.getElementById('current_dir');
  fetch('/files?dir=default')
  .then(function(response){
      return response.json();
  })
  .then(function(response){
    element.textContent=response;
    drawFolders('none',true);
  })
  
}


// Call the function to test

// Call the function to set up the event listener
