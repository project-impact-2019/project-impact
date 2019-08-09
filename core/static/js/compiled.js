(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
// Shorthand function for calling document.querySelector
function q (selector) {
    return document.querySelector(selector)
}

// Shorthand function for calling document.querySelectorAll
function qAll (selector) {
    return document.querySelectorAll(selector)
}



// Navigation Variables
const hamburger = q('.burger');
const nav = q('.nav-links');
const navLinks = qAll('.nav-links li');


// Main execution
document.addEventListener('DOMContentLoaded', function() {

    // Hamburger Style Navigation
hamburger.addEventListener('click', () => {

    nav.classList.toggle("nav-active");
    
    // Animate
    navLinks.forEach((link, index) =>{
        if(link.style.animation){
            link.style.animation = ' ';
        
        } else{
            link.style.animation = `navLinkFade 0.5s ease forwards ${index/7 + .2}s`
        }
        
    });
        
});
    
});


// Goals variables
const newGoal = q('.new_goal')
const newStep = qAll('.new_step')
const checkBox = qAll('.step-done-checkbox')
const goalCheckBox = qAll('.goal-done-checkbox')


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

goalCheckBox.forEach(item => {
    item.addEventListener('change', function (e) {
        // e.preventDefault();
        fetch(`goal/goal_check_mark/${item.dataset.goal}/`, {
            method: 'PATCH',
            body: JSON.stringify({ 'completed': item.checked }),
        })
        location.reload();
    })
})

const goals = document.querySelectorAll('.goal-div')
goals.forEach(item => {
    item.addEventListener('click', function (e) {
    const individualSteps = item.querySelectorAll('.individual-steps')
        individualSteps.forEach(step => { 
            step.innerHTML = `<div> ${step.dataset.step} </div>`
        });

        return individualSteps
    });

    });






var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
        panel.style.display = "none";
    } else {
        panel.style.display = "block";
    }
    });
}


// Progress bar
var ctx = document.getElementById('myChart').getContext('2d');
                var myChart = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                        labels: ['Goal 1', 'Goal 2', 'Goal 3', 'Goal 4', 'Goal 5', 'Goal 6'],
                        datasets: [{
                        label: '% of goal completed',
                        data: [100, 25, 100, 33, 0, 75],
                        backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                        }]
                },
                options: {
                        scales: {
                        yAxes: [{
                                ticks: {
                                beginAtZero: true,
                                max: 100
                                }
                        }]
                        }
                }
                });
},{}]},{},[1]);
