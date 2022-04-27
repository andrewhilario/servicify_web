var detail_btn = document.getElementById('continue');


if (detail_btn) {


    detail_btn.addEventListener('click', () => {
        location.href = "details"
    });

}

var account_type = document.getElementById('account_type');

if (account_type) {

    account_type.addEventListener('click', () => {
        location.href = "account-type"
    });


}


var worker = document.getElementById('worker');
var employer = document.getElementById('employer');

if (worker) {
    worker.addEventListener('click', () => {
        location.href = "success?type=worker"
    });
}
if (employer) {
    employer.addEventListener('click', () => {
        location.href = "success?type=employer"
    });
}


var scrollTop = document.getElementById('scroll-top');



window.onscroll = () => {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollTop.classList.remove('scroll-active-1');
        scrollTop.classList.add('scroll-active-2');
    } else {
        scrollTop.classList.remove('scroll-active-2');
        scrollTop.classList.add('scroll-active-1');


        if (scrollTop) {
            scrollTop.addEventListener('click', () => {

                window.scroll({ top: 0, left: 0, behavior: 'smooth' });
            });
        }
        console.log(window.scrollY);
    }
}
