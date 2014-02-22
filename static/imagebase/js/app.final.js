var ImagebaseRouter = Backbone.Router.extend({

    routes: {
        'image/:id/': 'viewImageDetail'
    },

    'viewImageDetail': function(id){
        var imageContentUrl = '/image/' + id + '/content/';
        console.log('load image %s:',id, imageContentUrl);
        $('#image-detail-container').load(imageContentUrl, null, function(){
            $('#image-master-container').removeClass('medium-12').addClass('medium-8');
        });
    }

});


$(function(){

    var imagebaseRouter = new ImagebaseRouter();

    $('a[data-pjax]').on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        console.log('e.currentTarget.pathname:', e.currentTarget.pathname);
        imagebaseRouter.navigate(e.currentTarget.pathname, {trigger: true});
    });

    Backbone.history.start({pushState: true});

});