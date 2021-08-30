const registrationForm = document.getElementById("registration-form")

var redirect = "/registration"

window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('sign-in-button', {
  'size': 'invisible',
  'callback': (response) => {
//     reCAPTCHA solved, allow signInWithPhoneNumber.
//    signInSuccessUrl:'/registration/',
    onSignInSubmit();
  }
});

document.getElementById('sign-in-button').click()

registrationForm.addEventListener('submit', (e) => {
    e.preventDefault()
    var phoneNumberInput = registrationForm['phone_number'].value.replace(/ /g, '')
    var countryCode = document.getElementsByClassName('iti__selected-dial-code')[0].innerHTML
    const phoneNumber = countryCode + phoneNumberInput;
    var phoneFormAction = registrationForm.action
    $.ajax({
        type: 'GET',
        url: `${phoneFormAction}`,
        data: {'phone_number': phoneNumber},
        success: function (response) {
            if (response['url']){
            redirectURL = response['url']
            const appVerifier = window.recaptchaVerifier;
            firebase.auth().signInWithPhoneNumber(phoneNumber, appVerifier)
                .then((confirmationResult) => {
                window.confirmationResult = confirmationResult;
                document.getElementById('changeble_div').innerHTML = `
                <div class="box__wrap">
                <div class="form__box">
                        <div class="form__box-head">
                            <h2 class="form__title">
                                Подтверждение номера
                                телефона
                            </h2>
                        </div>
                        <div class="check__number">
                            <div class="profile__icon">
                                <svg width="40" height="41" viewBox="0 0 40 41" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M36.0994 36.4314C35.1498 33.7735 33.0574 31.4248 30.1467 29.7497C27.2359 28.0746 23.6696 27.1666 20.0007 27.1666C16.3318 27.1666 12.7654 28.0746 9.85463 29.7497C6.94389 31.4248 4.85147 33.7735 3.90189 36.4314"
                                          stroke="#979797" stroke-width="3" stroke-linecap="round"/>
                                    <ellipse cx="19.9993" cy="13.8333" rx="8.33333" ry="8.33333" stroke="#979797"
                                             stroke-width="3" stroke-linecap="round"/>
                                </svg>
                            </div>
                            <div>
                                <p class="check__number-number">
                                    ${phoneNumber}
                                </p>
                                <a href="#" class="wrong__number" onclick="window.location.reload();">
                                    Неверный номер телефона?
                                </a>
                            </div>
                        </div>
                        <label class="form__input-wrap">
                            <input type="text" id="codeInput" class="form__input" placeholder="Введите код подтверждения" required>
                        </label>
                        <div id="error-message">
                        </div>
                        <button class="form__btn" type="submit" onclick=confirmCode()>
                            Отправить код
                        </button>
                        <a href="" class="no__sms">
                            Не пришло SMS сообщение?
                        </a>
                        <button class="sms__timer" type="submit" disabled>
                            Отправить снова через 0:<span class="timer__seconds">59</span>
                        </button>
                </div>
            </div>`;
                }).catch((error) => {
                grecaptcha.reset(window.recaptchaWidgetId);
                // Or, if you haven't stored the widget ID:
                window.recaptchaVerifier.render().then(function(widgetId) {
                grecaptcha.reset(widgetId);
                })
                });}else{
                    document.getElementById('error-message').innerHTML = `
                    <label style="color:red";>Этот номер телефона уже используется. Попробуйте другой.</label> <span id="error-message"></span>`
                }
        },
        error: function (error) {
        }
    })

})




function confirmCode() {
    var code = document.getElementById("codeInput").value;
    confirmationResult.confirm(code).then((result) => {
        const user = result.user;

        user.getIdToken(true).then(function (user_token) {
        localStorage.setItem('user_token', user_token)
        window.location.replace(redirect);
        });
      }).catch((error) => {
        document.getElementById('error-message').innerHTML = `
                    <label style="color:red";>Код не правильный. Повторите попытку</label> <span id="error-message"></span>`
      });
      signInSuccessUrl = redirect
}
