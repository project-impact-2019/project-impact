// Shorthand function for calling document.querySelector
function q (selector) {
    return document.querySelector(selector)
}

// Shorthand function for calling document.querySelectorAll
function qAll (selector) {
    return document.querySelectorAll(selector)
}

// Navigation Variables
const hamburger = q('.hamburger');
const navLinks = q('.nav-links');
const links = qAll('.nav-links li');


// Main execution for navigation bar
document.addEventListener('DOMContentLoaded', function() {

    // Hamburger Style Navigation
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle("open");
        links.forEach(link => {
            link.classList.toggle('fade');
        });
    });

});


// Goals variables
const newGoal = q('.new_goal')
const newStep = qAll('.new_step')
const checkBox = qAll('.step-done-checkbox')
console.log(checkBox)

// Main execution for goals

newGoal.addEventListener('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: $("#new_goal").attr('action'),
        data: {
            'description': $('.newGoal').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        // dataType: 'json',
        success: function (data) {
            // $(".goals").load(" .goals")
            location.reload();
        }
    });
});



// Drop down list menu

function toggleClass(elem,className){
	if (elem.className.indexOf(className) !== -1){
		elem.className = elem.className.replace(className,'');
	}
	else{
		elem.className = elem.className.replace(/\s+/g,' ') + 	' ' + className;
	}
	
	return elem;
}

function toggleDisplay(elem){
	const curDisplayStyle = elem.style.display;			
				
	if (curDisplayStyle === 'none' || curDisplayStyle === ''){
		elem.style.display = 'block';
	}
	else{
		elem.style.display = 'none';
	}
}


function toggleMenuDisplay(e){
	const dropdown = e.currentTarget.parentNode;
	const menu = dropdown.querySelector('.menu');
	const icon = dropdown.querySelector('.fa-angle-right');

	toggleClass(menu,'hide');
	toggleClass(icon,'rotate-90');
}

function handleOptionSelected(e){
	toggleClass(e.target.parentNode, 'hide');			

	const id = e.target.id;
	const newValue = e.target.textContent + ' ';
	const titleElem = document.querySelector('.dropdown .title');
	const icon = document.querySelector('.dropdown .title .fa');


	titleElem.textContent = newValue;
	titleElem.appendChild(icon);
	
	//trigger custom event
	document.querySelector('.dropdown .title').dispatchEvent(new Event('change'));
	//setTimeout is used so transition is properly shown
    setTimeout(() => toggleClass(icon,'rotate-90',0));

}

function handleTitleChange(e){
	const result = document.getElementById('result');

	result.innerHTML = 'The result is: ' + e.target.textContent;
}

//Trying to select item from goals

const getGoalItem = document.querySelectorAll('.goal-description')
// console.log(getGoalItem)


newStep.forEach(item => {
    item.addEventListener('submit', function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: item.action,
        data: {
            'goal': item.dataset.goal,
            'step': $(item).find('.newStep').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        // dataType: 'json',
        success: function (data) {
            // console.log('Success')
            // $(".goals").load(" .goals")
            location.reload();
        }
    });
});
})



checkBox.forEach(item => {
    item.addEventListener('change', function (e) {
        e.preventDefault();
        fetch(`goal/check_mark/${item.dataset.step}/`, {
            method: 'PATCH',
            body: JSON.stringify({ 'done': item.checked }),
        })
    })
})

        // $.ajax({
        //     type: 'POST',
        //     url: item.action,
        //     data: {
        //         'step': item.dataset.step,
        //         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        //     },
        //     // dataType: 'json',
        //     success: function (data) {
        //         // console.log('success')
        //         location.reload();
        //     } 
        // });
//     });
// });

// checkMark.forEach(item => {
//     item.addEventListener('submit', function (e) {
//     e.preventDefault();
//     console.log(item.dataset.step)
//     console.log(item.dataset.goal)
//     $.ajax({
//         type: 'POST',
//         url: item.action,
//         data: {
//             'step': item.dataset.step,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         },
//         dataType: 'json',
//         success: function (data) {
//             console.log('Success')
            // location.reload();
//         }
//     });
// });
// })