// var detail_btn = document.getElementById('continue');


// if (detail_btn) {


//     detail_btn.addEventListener('click', () => {
//         location.href = "details"
//     });

// }

// var account_type = document.getElementById('account_type');

// if (account_type) {

//     account_type.addEventListener('click', () => {
//         location.href = "account-type"
//     });


// }


// var worker = document.getElementById('worker');
// var employer = document.getElementById('employer');

// if (worker) {
//     worker.addEventListener('click', () => {
//         location.href = "success?type=worker"
//     });
// }
// if (employer) {
//     employer.addEventListener('click', () => {
//         location.href = "success?type=employer"
//     });
// }

function ready(fn) {
	if (document.readyState != 'loading') {
		fn();
	} else {
		document.addEventListener('DOMContentLoaded', fn);
	}
}

ready(() => {
	var scrollTop = document.getElementById('scroll-top');


	window.onload = () => {
		scrollTop.classList.add('scroll-active-1');
	}

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

	var workoffer = document.getElementById('workoffer');

	if (workoffer) {

		workoffer.onclick = () => {
			window.location.href = "/workoffer2"
		}
	}

	var acquireservice = document.getElementById('acquireservice');

	if (acquireservice) {

		acquireservice.onclick = () => {
			window.location.href = "/acquireservice2"
		}
	}


	var avatar = document.getElementById('avatar');
	var clicked_link = document.getElementById('navlinks-profile');


	if (avatar) {
		avatar.onclick = () => {
			clicked_link.classList.toggle('hover-profile-active');
		}
	}

	var workOfferCosts = document.getElementsByClassName('work-offer-cost-dashboard');
	for (let workOfferCost in workOfferCosts) {
		workOfferCost.innerText = parseInt(workOfferCost.innerText).toFixed(2);
	}


})

function myFunction(imgs) {
	var expandImg = document.getElementById("img-preview");
	expandImg.src = imgs.src;
	expandImg.parentElement.style.display = "block";
}







