var PageData = Backbone.Model.extend({
    url: '/dashboard/data/'
});

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
        var imageData = imageUrls[id],
            imageUpdateUrl = imageData.updateUrl,
            imageUrl = imageData.viewUrl;

        $('#modal').foundation('reveal', 'open', {url: imageUpdateUrl, animation_speed: 0});
        $(document).on('closed', '[data-reveal]', function () {
            imagebaseRouter.navigate(imageUrl, {trigger: true});
        });

    },

    'viewImage': function(id){
        var imageData = imageUrls[id],
            imageContentUrl = imageData.contentUrl;
        console.log('load image %s from %s', id, imageContentUrl);
        $('#modal').foundation('reveal', 'close');
        $('#image-detail-container').load(imageContentUrl, null, function(){
            $('#image-master-container').removeClass('medium-12').addClass('medium-8');
        });
    }

});


var imagebaseRouter = new ImagebaseRouter(),
    pageData = new PageData(),
    imageUrls;

$(function(){


    $('main').on('click', 'a[data-pjax]', function(e){
        e.preventDefault();
        e.stopPropagation();
        // console.log('e.currentTarget:', e.currentTarget);
        imagebaseRouter.navigate(e.currentTarget.pathname, {trigger: true});
    });

    pageData.fetch({
        success: function(model){
            imageUrls = model.get('images');
            console.log('imageUrls:', imageUrls);
            Backbone.history.start({pushState: true, root:'/dashboard/'});
        },
        error: function(e){
            console.log('error:', e);
        }
    });




});

