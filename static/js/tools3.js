// toggling between user and sample content
{
  function hasClass(element,check) {
    for (var i = 0; i < element.classList.length; i++) {
      if(element.classList[i] === check) {
        return true;
      }
    }
    return false;
  }

  (function toggleBetweenSampleUser() {
    let user_content = document.querySelector('.user-content');
    let sample_content = document.querySelector('.sample-content');
    let user_button = document.querySelector('.toggle-buttons-div').children[0];
    let sample_button = document.querySelector('.toggle-buttons-div').children[1];

    user_button.addEventListener('click',function() {
      if(!hasClass(user_content,"active-content")) {
          user_content.classList.toggle("active-content");
          sample_content.classList.toggle("active-content");
          user_button.classList.toggle("active-button");
          sample_button.classList.toggle("active-button");
      }
    });

    sample_button.addEventListener('click',function() {
      if(!hasClass(sample_content,"active-content")) {
          sample_content.classList.toggle("active-content");
          user_content.classList.toggle("active-content");
          user_button.classList.toggle("active-button");
          sample_button.classList.toggle("active-button");
      }
    })
  })();

// displaying the dropdown/dropup list
//    The dropdown list will open with a click on the button and close the
//    same way.

  (function dropdownControl() {
    let dropdown_button = Array.from(document.querySelectorAll('[data-show-list]'));
    dropdown_button.forEach(btn => {
      btn.addEventListener('click',function(event) {
        if (hasClass(btn.nextElementSibling,"selector-content-active")) {
          btn.nextElementSibling.classList.toggle("selector-content-active");
        }
        else {
          btn.nextElementSibling.classList.toggle("selector-content-active");
        }
      });
    });
  })();

// The dropdown would close if a mouse-click happens outside the event box
  (function closeDropdownByClickingOutsideTheBox() {
    document.addEventListener('click',function(event) {
      let to_close = document.querySelector('.selector-content-active');
      if (to_close !== null) {
        if (!to_close.contains(event.target.nextElementSibling)) {
          to_close.classList.toggle('selector-content-active');
        }
      }
    });
  })();

// Clicking one of the list elements, which would change the text
//    on the button and also close the dropdown (close the selector-content-active class)
let counter_for_change_of_text_on_buttons = {
  count_button_1: 0,
  count_button_2: 0,
  count_button_3: 0
};
  (function clickChangesButtonText() {
    let list_element = Array.from(document.querySelectorAll('[data-list]')); // data-list is a ul
    list_element.forEach(li => {
      let button_to_change = li.parentElement.previousElementSibling;
      let list_items = Array.from(li.children);
      list_items.forEach(item => {
        item.addEventListener('click',function(event) {
          button_to_change.innerText = this.innerText;
          button_to_change.nextElementSibling.classList.toggle('selector-content-active');
          if(button_to_change === document.querySelectorAll('[data-show-list]')[0]){
            openTheDropdownsBelow(button_to_change);
            counter_for_change_of_text_on_buttons.count_button_1 += 1;
          }
          else if (button_to_change === document.querySelectorAll('[data-show-list]')[1]) {
            counter_for_change_of_text_on_buttons.count_button_2 += 1;
          }
          else if (button_to_change === document.querySelectorAll('[data-show-list]')[2]) {
            counter_for_change_of_text_on_buttons.count_button_3 += 1;
          }
// if all the selectors have at least one options selected, then the align button would
  // be enabled
          if (counter_for_change_of_text_on_buttons.count_button_1 >= 1 &&
                counter_for_change_of_text_on_buttons.count_button_2 >= 1 &&
                counter_for_change_of_text_on_buttons.count_button_3 >= 1)
          {
            let align_button = document.querySelectorAll('.footer-buttons')[0].children[0];
            align_button.disabled = false;
          }
        })
      });
    });
  })();

// Only when the first select options is chosen, would the other select options become
// enabled along with the textarea.

  function openTheDropdownsBelow(button_that_changed) {
    let textarea = document.querySelector('textarea');
    textarea.disabled = false;
    let buttons_to_be_enabled = (Array.from(document.querySelectorAll('[data-show-list]'))).slice(1);
    buttons_to_be_enabled.forEach(btn => {
      btn.disabled = false;
    });
  }

// resetting the textarea upon the click of the reset button
  (function resettingTextarea() {
    let reset_btn = document.querySelectorAll('.footer-buttons')[0].children[1];
    let textarea = document.querySelector('textarea');
    reset_btn.addEventListener('click',function() {
      textarea.value = "";
      console.log(textarea);
    })
  })();
}
