(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
// Shorthand function for calling document.querySelector
function q (selector) {
    return document.querySelector(selector)
}

// Shorthand function for calling document.querySelectorAll
function qAll (selector) {
    return document.querySelectorAll(selector)
}

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

// Main execution for goals

newGoal.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log(newGoal)
    $.ajax({
        type: 'POST',
        url: $("#new_goal").attr('action'),
        data: {
            'description': $('.newGoal').val(),
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


newStep.forEach(item => {
    item.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log(item.action)
    console.log(item.dataset.goal)
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


      
},{}]},{},[1]);
