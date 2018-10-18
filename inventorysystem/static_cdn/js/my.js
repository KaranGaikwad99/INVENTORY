$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-entries').modal('show');
			},
			success: function(data){
				$('#modal-entries .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#entries-table tbody').html(data.entries_list);
					$('#modal-entries').modal('hide');
				} else {
					$('#modal-entries .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	};

// create 
$(".show-form").click(ShowForm);
$("#modal-entries").on("submit",".create-form",SaveForm);

//update
$('#entries-table').on("click",".show-form-update",ShowForm);
$('#modal-entries').on("submit",".update-form",SaveForm);

//delete
$('#entries-table').on("click",".show-form-delete",ShowForm);
$('#modal-entries').on("submit",".delete-form",SaveForm);

// For date picker
$('.schemedatepicker').datepicker({
	autoclose:true,
});
});

 
