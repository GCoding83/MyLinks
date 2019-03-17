


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

$(function(){
	$('.box-bottom').on('click', function(){	
		$(this).next().toggle(100);
	});
});

$(function(){
	$('.box-top').on('click', function(){	
		$(this).prev().toggle(100);
	});
});


$(function(){
	$('.nested-citations').on('click', function(){	
		$(this).next().toggle(100);
	});
});



/*The jQuery for opening the citation abstracts in the bottom-right and top-right boxes*/
$(function(){
	/*When user clicks on a citation-description of a publication*/
	$('body').on('click', '.citation-description', function(){
		/*Declare the variables that store the unique id'd of each author and abstract of the clicked description */
		var authorid = "author" + $(this).attr('id');
		var abstractid = "abstract" + $(this).attr('id');
		var box = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open');
		/*Declare nearest other citation abstracts and authors*/
		var otherauthor = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-author');
		var otherabstract = $(this).closest('.box-bottom-open').siblings('.box-bottom-right-open').find('.bottom-right-abstract');

		/*if clicked citation abstract is not showing*/
		if ($("#"+abstractid).is(':hidden')) {	
/*			if there already is another citation abstract showing (meaning the box is open)		
*/			if (otherabstract.is(':visible')) {
				/*Hide the currently showing abstract (and related author)*/
				$(otherabstract).hide();
				$(otherauthor).hide();
				/*Show the clicked abstract and author*/
				$("#"+authorid).show();
				$("#"+abstractid).show();
/*			else if no other citation abstract is showing (meaning the box is closed)
*/			} else {
				/*Show the clicked citation abstract (and author) and open the box*/
				$("#"+authorid).show();
				$("#"+abstractid).show();
				$(box).show();
			}
/*		else if clicked citation abstract is already showing (meaning you want to close the box)
*/		} else {
/*			close everything
*/			$("#"+authorid).hide();
			$("#"+abstractid).hide();
			$(box).hide();
		}
	});
});