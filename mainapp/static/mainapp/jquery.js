$(function(){
	$('.box-right').on('click', function(){	
		$(this).next().toggle(100);
	});
});

$(function(){
	$('.box-left').on('click', function(){	
		var $open = $(this).prev()
		$open.toggle(100);
		if ($open.attr('display') == 'none'){
			alert("Hello");
		} 
	});
});

/*When user clicks on the bar with the logo, open the bottom box ("box-bottom-open")*/
$(function(){
	$('.box-bottom').on('click', function(){	
		/*Toggle the bottom box ("box-bottom-open")*/
		$(this).next().toggle(100);

		/*Ensure that the bottom-right and bottom-left boxes (the one with the citation abstracts and the one with the citation infos) get closed if the bottom-box (the one with the logo) is closed*/
		var bottomRightBox = $(this).siblings('.box-bottom-right-open');
		var bottomLeftBox = $(this).siblings('.box-bottom-left-open');
		/*Declare the images that need to be small when user closes the bottom box*/
		var anyAbstractImage = $(this).next().find('.bottom-abstract-image');
		var anyInfoImage = $(this).next().find('.bottom-info-image');		
		/*Declare ANY citation abstracts and authors in this box*/
		var anyBottomRightBoxAuthor = $(this).siblings('.box-bottom-right-open').find('.bottom-right-author');
		var anyBottomRightBoxAbstract = $(this).siblings('.box-bottom-right-open').find('.bottom-right-abstract');
		/*Declare ANY citation infos and authors in this box*/
		var anyBottomLeftBoxAuthor = $(this).siblings('.box-bottom-left-open').find('.bottom-left-author');
		var anyBottomLeftBoxInfo = $(this).siblings('.box-bottom-left-open').find('.bottom-left-info');
		
		
		if ($(bottomRightBox).is(':visible')){
/*			close everything, and make the images smaller
*/			$(anyBottomRightBoxAbstract).hide();
			$(anyBottomRightBoxAuthor).hide();
			$(bottomRightBox).hide();
			$(anyAbstractImage).removeClass('image-active');	
		}
		if ($(bottomLeftBox).is(':visible')){
/*			close everything, and make the images smaller
*/			$(anyBottomLeftBoxInfo).hide();
			$(anyBottomLeftBoxAuthor).hide();
			$(bottomLeftBox).hide();
			$(anyInfoImage).removeClass('image-active');	
		}

	});
});

$(function(){
	$('.box-top').on('click', function(){	
		$(this).prev().toggle(100);
	});
});


/*When user clicks on the citation in the bottom box, open the citation description.*/
$(function(){
	$('.nested-citations').on('click', function(){		
		/*Declare the box-bottom-right-open*/
		var bottomRightBox = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open');
		var bottomLeftBox = $(this).closest('.box-bottom-open').siblings('.box-bottom-left-open');

		/*Declare this citation's bottom-RIGHT id's, i.e. abstract and author id's*/
		var thisBottomRightAbstractId = "bottomRightAbstract" + $(this).next().attr('id');
		var thisBottomRightAuthorId = "bottomRightAuhtor" + $(this).next().attr('id');		
	
		/*Declare this citation's bottom-LEFT id's, i.e. info and author id's*/
		var thisBottomLeftInfoId = "bottomLeftInfo" + $(this).next().attr('id');
		var thisBottomLeftAuthorId = "bottomLeftAuhtor" + $(this).next().attr('id');		
		
		/*Declare ANY citation abstracts and authors in this box*/
		var anyBottomRightAuthor = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-author');
		var anyBottomRightAbstract = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-abstract');
	
		/*Declare ANY citation info and authors in this box*/
		var anyBottomLeftAuthor = $(this).closest('.box-bottom-open').siblings('.box-bottom-left-open').find('.bottom-left-author');
		var anyBottomLeftInfo = $(this).closest('.box-bottom-open').siblings('.box-bottom-left-open').find('.bottom-left-info');
	
		/*The abstract image associated with the citation description*/
		var thisAbstractImage = $(this).next().find('.bottom-abstract-image');

		/*The abstract image associated with the citation description*/
		var thisInfoImage = $(this).next().find('.bottom-info-image');

		/*if clicked citation abstract is already showing (in the RIGHT box)*/
		if ($("#"+thisBottomRightAbstractId).is(':visible')) {	
			/*if clicked citation info is also showing (in the LEFT box)*/
			/*i.e. if BOTH left and right are showing*/
			if ($("#"+thisBottomLeftInfoId).is(':visible')) {	
				/*close everything, both left and right, and make sure images are small*/			
				$(anyBottomRightAbstract).hide();
				$(anyBottomRightAuthor).hide();
				$(bottomRightBox).hide();
				$(thisAbstractImage).removeClass('image-active');
				$(anyBottomLeftInfo).hide();
				$(anyBottomLeftAuthor).hide();
				$(bottomLeftBox).hide();
				$(thisInfoImage).removeClass('image-active');
				$(this).next().hide(100);
			/*if clicked citation abstract alone is showing (in the RIGHT box*/
			} else {
				/*Close everything on the right*/
				$(anyBottomRightAbstract).hide();
				$(anyBottomRightAuthor).hide();
				$(bottomRightBox).hide();
				$(thisAbstractImage).removeClass('image-active');
				$(this).next().hide(100);
			}
		/*else if only the clicked citation info is showing (in the LEFT box)*/
		} else if ($("#"+thisBottomLeftInfoId).is(':visible')){
			/*Close everything on the left*/
			$(anyBottomLeftInfo).hide();
			$(anyBottomLeftAuthor).hide();
			$(bottomLeftBox).hide();
			$(thisInfoImage).removeClass('image-active');
			$(this).next().hide(100);
		
		/*else if neither is visible, on the left or right, then simply toggle the citation description */
		} else {
			$(this).next().toggle(100);
		}
	});	
});



/*Below is the main function for the BOTTOM-RIGHT (i.e. abstract) box*/
/*When user clicks on the abstract image in the bottom box, open the bottom right box.*/
$(function(){
	/*When user clicks on a citation-description of a publication*/
	$('body').on('click', '.bottom-abstract-image', function(){
		/*Declare the variables that store the unique id'd of each author and abstract of the clicked description */
		var thisAuthorId = "bottomRightAuthor" + $(this).closest('.citation-description').attr('id');
		var thisAbstractId = "bottomRightAbstract" + $(this).closest('.citation-description').attr('id');
		/*Declare ANY citation abstracts and authors in this box*/
		var anyBoxAuthor = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-author');
		var anyBoxAbstract = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-abstract');
		/*Declare ANY abstract image in this box*/
		var anyAbstractImage = $(this).closest('.box-bottom-open').find('.bottom-abstract-image');
		/*Declare the main box-bottom-right-open box*/
		var box = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open');
		


		/*if clicked citation abstract is not showing*/
		if ($("#"+thisAbstractId).is(':hidden')) {	
/*			if there already is another citation abstract showing (meaning the box is open)		
*/			if (anyBoxAbstract.is(':visible')) {
				/*Make all abstract images regular size and hide the currently showing abstract (and related author)*/
				$(anyAbstractImage).removeClass('image-active');
				$(anyBoxAbstract).hide();
				$(anyBoxAuthor).hide();

				/*Make this abstract image bigger and show the clicked abstract and author*/
				$(this).addClass('image-active');
				$("#"+thisAuthorId).show();
				$("#"+thisAbstractId).show();
/*			else if no other citation abstract is showing (meaning the box is closed)
*/			} else {
				/*Make this abstract image bigger and show the clicked citation abstract (and author) and open the box*/
				$(this).addClass('image-active');
				$("#"+thisAuthorId).show();
				$("#"+thisAbstractId).show();
				$(box).show();
			}
/*		else if clicked citation abstract is already showing (meaning you want to close the box)
*/		} else {
/*			close everything
*/			$(this).removeClass('image-active');
			$("#"+thisAuthorId).hide();
			$("#"+thisAbstractId).hide();
			$(box).hide();
		}
	});
});


/*Below is the main function for the BOTTOM-LEFT (i.e. info) box*/
/*When user clicks on the info image in the bottom box, open the bottom right box.*/
$(function(){
	/*When user clicks on a citation-description of a publication*/
	$('body').on('click', '.bottom-info-image', function(){
		/*Declare the variables that store the unique id'd of each author and info of the clicked description */
		var thisAuthorId = "bottomLeftAuthor" + $(this).closest('.citation-description').attr('id');
		var thisInfoId = "bottomLeftInfo" + $(this).closest('.citation-description').attr('id');
		/*Declare ANY citation info and authors in this box*/
		var anyBoxAuthor = $(this).closest('.box-bottom-open').siblings('.box-bottom-left-open').find('.bottom-left-author');
		var anyBoxInfo = $(this).closest('.box-bottom-open').siblings('.box-bottom-left-open').find('.bottom-left-info');
		/*Declare ANY info image in this box*/
		var anyInfoImage = $(this).closest('.box-bottom-open').find('.bottom-info-image');
		/*Declare the main box-bottom-right-open box*/
		var box = $(this).closest('.box-bottom-open').siblings('.box-bottom-left-open');
		
		/*if clicked citation info is not showing*/
		if ($("#"+thisInfoId).is(':hidden')) {	
/*			if there already is another citation info showing (meaning the box is open)		
*/			if (anyBoxInfo.is(':visible')) {
				/*Make all abstract images regular size and hide the currently showing info (and related author)*/
				$(anyInfoImage).removeClass('image-active');
				$(anyBoxInfo).hide();
				$(anyBoxAuthor).hide();

				/*Make this info image bigger and show the clicked abstract and author*/
				$(this).addClass('image-active');
				$("#"+thisAuthorId).show();
				$("#"+thisInfoId).show();
/*			else if no other citation info is showing (meaning the box is closed)
*/			} else {
				/*Make this info image bigger and show the clicked citation info (and author) and open the box*/
				$(this).addClass('image-active');
				$("#"+thisAuthorId).show();
				$("#"+thisInfoId).show();
				$(box).show();
			}
/*		else if clicked citation info is already showing (meaning you want to close the box)
*/		} else {
/*			close everything
*/			$(this).removeClass('image-active');
			$("#"+thisAuthorId).hide();
			$("#"+thisInfoId).hide();
			$(box).hide();
		}
	});
});