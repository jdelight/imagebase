var ImagebaseRouter = Backbone.Router.extend({

    routes: {
        '': 'viewDashboard',
        'image/:id/': 'viewImageDetail'
    },

    'viewDashboard': function(){
        $('#image-detail-container').empty();
        $('#image-master-container').removeClass('medium-8').addClass('medium-12');
    },

    'viewImageDetail': function(id){
        var imageContentUrl = '/image/' + id + '/content/';
        console.log('load image %s from %s', id, imageContentUrl);
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
        imagebaseRouter.navigate(e.currentTarget.pathname, {trigger: true});
    });

    Backbone.history.start({pushState: true, root:'/dashboard/'});

});

