/*Handling the right box*/
$(function(){
	$('.right-box').on('click', function(){	
		$(this).next().toggle(100);
	});
});

/*Handling the left box*/
$(function(){
	$('.left-box').on('click', function(){	
		var $open = $(this).prev()
		$open.toggle(100);
		if ($open.attr('display') == 'none'){
			alert("Hello");
		} 
	});
});



/*BELOW ARE THE FOUR MAIN FUNCTIONS FOR HANDLING THE TOP AND BOTTOM BOX BEHAVIORS.*/
/*1. The first handles box behavior when user clicks on ".top-box" or ".bottom-box", i.e. the boxes with the quotation logos*/
/*2. The second handles box behavior when user clicks on ".top-nested-citations" or ".bottom-nested-citations", which opens the citation description*/
/*3. The third handles box behavior when user clicks on ".top-abstract-image" or ".bottom-abstract-image", which opens the abstract box on the bottom-right or top-right */
/*4. The fourth handles box behavior when user clicks on ".top-info-image" or ".bottom-info-image", which opens the details box on the bottom-left or top-left */


/*1.*/
/*When user clicks on the bar with the quotes logo,  WHETHER TOP-BOX OR BOTTOM-BOX, toggle the box below ("top-box-open" or "bottom-box-open")*/
$(function(){
	$('.top-box, .bottom-box').on('click', function(){	
		/*Toggle the next box ("top-box-open" or "bottom-box-open")*/
		$(this).next().toggle(100);

		/*Variable to determine whether the clicked box is a top or bottom one*/
		if ($(this).is('.top-box')){
			var vertical = 'top';
		} else {
			var vertical = 'bottom';
		}

		/*Ensure that the top/bottom-right and top/bottom-left boxes (the one with the citation abstracts and the one with the citation infos) get closed if the top-box (the one with the logo) is closed*/
		var rightBox = $(this).siblings('.'+vertical+'-right-box-open');
		var leftBox = $(this).siblings('.'+vertical+'-left-box-open');
		/*Declare the images that need to be small when user closes the top/bottom box*/
		var anyAbstractImage = $(this).next().find('.'+vertical+'-abstract-image');
		var anyInfoImage = $(this).next().find('.'+vertical+'-info-image');		
		/*Declare ANY citation abstracts and authors in this box*/
		var anyRightBoxAuthor = $(this).siblings('.'+vertical+'-right-box-open').find('.'+vertical+'-right-author');
		var anyRightBoxAbstract = $(this).siblings('.'+vertical+'-right-box-open').find('.'+vertical+'-right-abstract');
		/*Declare ANY citation infos and authors in this box*/
		var anyLeftBoxAuthor = $(this).siblings('.'+vertical+'-left-box-open').find('.'+vertical+'-left-author');
		var anyLeftBoxInfo = $(this).siblings('.'+vertical+'-left-box-open').find('.'+vertical+'-left-info');
		
		
		if ($(rightBox).is(':visible')){
/*			close everything, and make the images smaller
*/			$(anyRightBoxAbstract).hide();
			$(anyRightBoxAuthor).hide();
			$(rightBox).hide();
			$(anyAbstractImage).removeClass('image-active');	
		}
		if ($(leftBox).is(':visible')){
/*			close everything, and make the images smaller
*/			$(anyLeftBoxInfo).hide();
			$(anyLeftBoxAuthor).hide();
			$(leftBox).hide();
			$(anyInfoImage).removeClass('image-active');	
		}

	});
});


/*2.*/
/*When user clicks on the citation in the top/bottom box, open the citation description and make the text bold and bigger.*/
$(function(){
	$('.top-nested-citations, .bottom-nested-citations').on('click', function(){	
		
		/*Variable to determine whether the clicked box is a top or bottom one*/
		if ($(this).is('.top-nested-citations')){
			var vertical = 'top';
		} else {
			var vertical = 'bottom';
		}

		/*Declare the top/bottom-right-box-open*/
		var rightBox = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-right-box-open');
		var leftBox = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-left-box-open');

		/*Declare this citation's top/bottom-RIGHT id's, i.e. abstract and author id's*/
		var thisRightAbstractId = vertical+"RightAbstract" + $(this).next().attr('id');
		var thisRightAuthorId = vertical+"RightAuhtor" + $(this).next().attr('id');		
	
		/*Declare this citation's top/bottom-LEFT id's, i.e. info and author id's*/
		var thisLeftInfoId = vertical+"LeftInfo" + $(this).next().attr('id');
		var thisLeftAuthorId = vertical+"LeftAuhtor" + $(this).next().attr('id');		
		
		/*Declare ANY citation abstracts and authors in this box*/
		var anyRightAuthor = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-right-box-open').find('.'+vertical+'-right-author');
		var anyRightAbstract = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-right-box-open').find('.'+vertical+'-right-abstract');
	
		/*Declare ANY citation info and authors in this box*/
		var anyLeftAuthor = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-left-box-open').find('.'+vertical+'-left-author');
		var anyLeftInfo = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-left-box-open').find('.'+vertical+'-left-info');
	
		/*The abstract image associated with the citation description*/
		var thisAbstractImage = $(this).next().find('.'+vertical+'-abstract-image');

		/*The abstract image associated with the citation description*/
		var thisInfoImage = $(this).next().find('.'+vertical+'-info-image');

		/*if clicked citation abstract is already showing (in the RIGHT box)*/
		if ($("#"+thisRightAbstractId).is(':visible')) {	
			/*if clicked citation info is also showing (in the LEFT box)*/
			/*i.e. if BOTH left and right are showing*/
			if ($("#"+thisLeftInfoId).is(':visible')) {	
				/*close everything, both left and right, and make sure images are small and fonts are small*/			
				$(anyRightAbstract).hide();
				$(anyRightAuthor).hide();
				$(rightBox).hide();
				$(thisAbstractImage).removeClass('image-active');
				$(anyLeftInfo).hide();
				$(anyLeftAuthor).hide();
				$(leftBox).hide();
				$(thisInfoImage).removeClass('image-active');
				$(this).removeClass('citation-active').addClass(vertical+'-nested-citations');
				$(this).next().hide(100);
			/*if clicked citation abstract alone is showing (in the RIGHT box*/
			} else {
				/*Close everything on the right*/
				$(anyRightAbstract).hide();
				$(anyRightAuthor).hide();
				$(rightBox).hide();
				$(thisAbstractImage).removeClass('image-active');
				$(this).removeClass('citation-active').addClass(vertical+'-nested-citations');
				$(this).next().hide(100);
			}
		/*else if only the clicked citation info is showing (in the LEFT box)*/
		} else if ($("#"+thisLeftInfoId).is(':visible')){
			/*Close everything on the left*/
			$(anyLeftInfo).hide();
			$(anyLeftAuthor).hide();
			$(leftBox).hide();
			$(thisInfoImage).removeClass('image-active').addClass(vertical+'-nested-citations');
			$(this).removeClass('citation-active');
			$(this).next().hide(100);
		
		/*else if neither is visible, on the left or right, then simply toggle the citation description */
		} else {
			$(this).next().toggle(100);
			if ($(this).hasClass('citation-active')){
				$(this).removeClass('citation-active').addClass(vertical+'-nested-citations');
			}else{
				$(this).removeClass(vertical+'-nested-citations').addClass('citation-active');
			}
		}
	});	
});


/*3.*/
/*Below is the main function for the TOP/BOTTOM-RIGHT (i.e. abstract) box*/
/*When user clicks on the abstract image in the top/bottom box, open the top/bottom right box.*/
$(function(){
	/*When user clicks on a the abstract image of a publication*/
	$('body').on('click', '.top-abstract-image, .bottom-abstract-image', function(){
		
		/*Variable to determine whether the clicked box is a top or bottom one*/
		if ($(this).is('.top-abstract-image')){
			var vertical = 'top';
		} else {
			var vertical = 'bottom';
		}

		/*Declare the variables that store the unique id'd of each author and abstract of the clicked description */
		var thisAuthorId = vertical+"RightAuthor" + $(this).closest('.citation-description').attr('id');
		var thisAbstractId = vertical+"RightAbstract" + $(this).closest('.citation-description').attr('id');
		/*Declare ANY citation abstracts and authors in this box*/
		var anyBoxAuthor = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-right-box-open').find('.'+vertical+'-right-author');
		var anyBoxAbstract = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-right-box-open').find('.'+vertical+'-right-abstract');
		/*Declare ANY abstract image in this box*/
		var anyAbstractImage = $(this).closest('.'+vertical+'-box-open').find('.'+vertical+'-abstract-image');
		/*Declare the main top/bottom-right-box-open box*/
		var box = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-right-box-open');
		


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


/*4.*/
/*Below is the main function for the TOP/BOTTOM-LEFT (i.e. info) box*/
/*When user clicks on the info image in the top/bottom box, open the top/bottom right box.*/
$(function(){
	/*When user clicks on a citation-description of a publication*/
	$('body').on('click', '.top-info-image, .bottom-info-image', function(){

		/*Variable to determine whether the clicked box is a top or bottom one*/
		if ($(this).is('.top-info-image')){
			var vertical = 'top';
		} else {
			var vertical = 'bottom';
		}

		/*Declare the variables that store the unique id'd of each author and info of the clicked description */
		var thisAuthorId = vertical+"LeftAuthor" + $(this).closest('.citation-description').attr('id');
		var thisInfoId = vertical+"LeftInfo" + $(this).closest('.citation-description').attr('id');
		/*Declare ANY citation info and authors in this box*/
		var anyBoxAuthor = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-left-box-open').find('.'+vertical+'-left-author');
		var anyBoxInfo = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-left-box-open').find('.'+vertical+'-left-info');
		/*Declare ANY info image in this box*/
		var anyInfoImage = $(this).closest('.'+vertical+'-box-open').find('.'+vertical+'-info-image');
		/*Declare the main box-top-right-open box*/
		var box = $(this).closest('.'+vertical+'-box-open').siblings('.'+vertical+'-left-box-open');
		
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