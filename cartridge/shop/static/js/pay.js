$(document).ready(function() { 


if ( $( "#card-number" ).length ) {

var key = document.head.querySelector('meta[name=stripe_PublicKey]').content;

// Create a Stripe client
var stripe = Stripe(key);

// Create an instance of Elements
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
  base: {
    color: '#32325d',
    lineHeight: '24px',
    fontFamily: 'Arial, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};

// Create an instance of the card Element
var num = elements.create('cardNumber');

// Add an instance of the card Element into the `card-element` <div>
num.mount('#card-number');

var exp = elements.create('cardExpiry', {style: style});

exp.mount('#card-expiry');

var cvc = elements.create('cardCvc', {style: style});

cvc.mount('#card-cvc');

var pcod = elements.create('postalCode', {style: style});

pcod.mount('#card-postalCode');



function setOutcome(result) {
  var errorElement = document.getElementById('card-errors');   
  errorElement.textContent = '';    
  errorElement.classList.add('hide'); 
    
    if (result.error) {
      errorElement.textContent = result.error.message; 
      errorElement.classList.remove('hide');  
      
      // Reenable the submit button
      document.querySelector("#proceed").disabled = false;
      
  } else if (result.token) {
        stripeTokenHandler(result.token);
  }

}


// Handle real-time validation errors from the card Element.
num.addEventListener('change', function(event) {
  setOutcome(event);
});

// Handle real-time validation errors from the card Element.
exp.addEventListener('change', function(event) {
  setOutcome(event);
});

cvc.addEventListener('change', function(event) {
  setOutcome(event);
});

// Handle real-time validation errors from the card Element.
pcod.addEventListener('change', function(event) {
 setOutcome(event);
});

// Handle form submission
var form = document.getElementById('checkout-form');
form.addEventListener('submit', function(event) {
  
  event.preventDefault();   
  
  // Disable the submit button to avoid creating multiple tokens
  document.querySelector("#proceed").disabled = true;

  stripe.createToken(num).then(function(result) {
    setOutcome(result);
  });
});


function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server
  var form = document.getElementById('checkout-form');
  var hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripe_token');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
};


}





});