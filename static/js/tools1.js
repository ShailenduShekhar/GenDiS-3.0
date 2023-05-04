// For toggling between User and Sample content
{
  function hasClass(element,check_class) {
    for (var i = 0; i < element.classList.length; i++) {
      if(element.classList[i] === check_class) {
        return true;
      }
    }
    return false;
  }
  let user_button = document.getElementsByClassName('options-button')[0];
  let sample_button = document.getElementsByClassName('options-button')[1];

  sample_button.addEventListener('click',function() {
    sample_content = document.querySelector('.sample-content');
    if(!hasClass(sample_content,"active")) {
      sample_content.classList.toggle('active');
      sample_content.previousElementSibling.classList.toggle('active');
      sample_button.classList.toggle("options-button-active");
      user_button.classList.toggle("options-button-active");
    }
  })
  user_button.addEventListener('click',function() {
    user_content = document.querySelector('.user-content');
    if(!hasClass(user_content,"active")) {
      user_content.classList.toggle('active');
      user_content.nextElementSibling.classList.toggle('active');
      sample_button.classList.toggle("options-button-active");
      user_button.classList.toggle("options-button-active");
    }
  })

  // For Reset button
  reset_btn = document.querySelectorAll('[data-button-type="reset"]');
  console.log(reset_btn);
  console.log(document.querySelector('textarea'));
  for (var i = 0; i < reset_btn.length; i++) {
    reset_btn[i].addEventListener('click',function() {
      textarea = document.querySelector('textarea');
      if(textarea.innerText !== "") {
        console.log("hey");
        textarea.innerText = "";
      }
    })
  }
}
