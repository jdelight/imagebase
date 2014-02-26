var ImagebaseRouter = Backbone.Router.extend({

    routes: {
        '': 'viewDashboard',
        'image/:id/': 'viewImage',
        'image/:id/update/': 'updateImage'
    },

    'viewDashboard': function(){
        $('#image-detail-container').empty();
        $('#image-master-container').removeClass('medium-8').addClass('medium-12');
    },

    'updateImage': function(id){
        console.log('update image %s:', id);
        var imageUpdateUrl = '/image/' + id + '/update/content/';
        var imageUrl = '/image/' + id + '/';
        var router = this;

        $('#modal').foundation('reveal', 'open', {url: imageUpdateUrl, animation_speed: 0});
        $(document).on('closed', '[data-reveal]', function () {
            router.navigate(imageUrl, {trigger: true});
        });

    },

    'viewImage': function(id){
        var imageContentUrl = '/image/' + id + '/content/';
        console.log('load image %s from %s', id, imageContentUrl);
        $('#modal').foundation('reveal', 'close');
        $('#image-detail-container').load(imageContentUrl, null, function(){
            $('#image-master-container').removeClass('medium-12').addClass('medium-8');
        });
    }

});


$(function(){

    var imagebaseRouter = new ImagebaseRouter();

    $('main').on('click', 'a[data-pjax]', function(e){
        e.preventDefault();
        e.stopPropagation();
        // console.log('e.currentTarget:', e.currentTarget);
        imagebaseRouter.navigate(e.currentTarget.pathname, {trigger: true});
    });

    Backbone.history.start({pushState: true, root:'/dashboard/'});

});

