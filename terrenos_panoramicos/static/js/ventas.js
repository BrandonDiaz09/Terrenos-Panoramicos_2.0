$( document ).ready(function() {
    $('.meInteresa_form').submit(function(e){
        e.preventDefault();

        const inmueble_id = $(this).attr('id')
        //const corazon = $('.dd${inmueble_id}').txt()
        
        const url =$(this).attr('action')
        const boton = $('button',this)
        const corazon = $('button',this).hasClass("icono")
        let heart_main = '<svg class="heart-main" viewBox="0 0 512 512" width="30" title="heart"><path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z" /></svg>'
        let heart_background = '<svg class="heart-background" viewBox="0 0 512 512" width="30" title="heart"><path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z" /></svg>'
        datos = []

        $.ajax({
          type: 'POST',
          url : url,
          data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'inmueble_id':inmueble_id,
          },
          success: function(response){
            console.log('succes', response)
            console.log(corazon)
            if (corazon){
              boton.addClass("icono_active")
              boton.removeClass("icono")
              boton.html(heart_main)
            }
            else{
              boton.addClass("icono")
              boton.removeClass("icono_active")
              boton.html(heart_main + heart_background)
            }
            

           
          //boton.html('<i>Hola!</i>');    
          

            
            // if(corazon == 'icono'){
            //   $('.Strong').html('action')
            // }
          },
          error: function(response){
            console.log('error',response)
          }
        });   
    })
})