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
		$(this).next().toggle(100);
		/*Ensure that the bottom-right box (the one with the citation abstracts) gets closed if the bottom-box (the one with the logo) is closed*/
		var box = $(this).siblings('.box-bottom-right-open');
		/*Declare the images that need to be small when user closes the bottom box*/
		var anyAbstractImage = $(this).next().find('.bottom-abstract-image');
		/*Declare ANY citation abstracts and authors in this box*/
		var anyBoxAuthor = $(this).siblings('.box-bottom-right-open').find('.bottom-right-author');
		var anyBoxAbstract = $(this).siblings('.box-bottom-right-open').find('.bottom-right-abstract');
		
		if ($(box).is(':visible')){
/*			close everything, and make the images smaller
*/			$(anyBoxAbstract).hide();
			$(anyBoxAuthor).hide();
			$(box).hide();
			$(anyAbstractImage).removeClass('image-active');	
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
		/*Declare this citation's abstract and author id's*/
		var thisAbstractId = "abstract" + $(this).next().attr('id');
		var thisAuthorId = "auhtor" + $(this).next().attr('id');		
		/*Declare ANY citation abstracts and authors in this box*/
		var anyBoxAuthor = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-author');
		var anyBoxAbstract = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-abstract');
		/*Declare the box-bottom-right-open*/
		var box = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open');
		/*The abstract image associated with the citation description*/
		var thisAbstractImage = $(this).next().find('.bottom-abstract-image');

		/*if clicked citation abstract is already showing*/
		if ($("#"+thisAbstractId).is(':visible')) {	
			/*close everything, including this citation's description and make sure images are small*/			
			$(anyBoxAbstract).hide();
			$(anyBoxAuthor).hide();
			$(box).hide();
			$(thisAbstractImage).removeClass('image-active');
			$(this).next().hide(100);

/*		else if clicked citation abstract is not showing, just toggle the citation description
*/		} else {
			$(this).next().toggle(100);
		}
	});	
});



/*When user clicks on the citation abstracts in the bottom box, open the bottom right box.*/
$(function(){
	/*When user clicks on a citation-description of a publication*/
	$('body').on('click', '.bottom-abstract-image', function(){
		/*Declare the variables that store the unique id'd of each author and abstract of the clicked description */
		var thisAuthorId = "author" + $(this).closest('.citation-description').attr('id');
		var thisAbstractId = "abstract" + $(this).closest('.citation-description').attr('id');
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