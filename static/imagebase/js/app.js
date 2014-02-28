var PageData = Backbone.Model.extend({
    url: '/dashboard/data/'
});
var useReplaceState = false;
var ImagebaseRouter = Backbone.Router.extend({

    routes: {
        '': 'viewDashboard',
        'image/:id/': 'viewImage',
        'image/:id/update/': 'updateImage',
        'image/:id/delete/': 'deleteImage'
    },

    'viewDashboard': function(){
        imagebaseRouter.resetView();
        $('#image-master-container').addClass('medium-12').removeClass('medium-8');
        useReplaceState = false;
    },

    'updateImage': function(id){
        var imageData = imageUrls[id],
            imageUpdateUrl = imageData.updateUrl;

        $('#image-update-container').load(imageUpdateUrl, null, function(){
            imagebaseRouter.prepGridForSidePanel();
            $(this).parent().removeClass('returned').addClass('flipped');


            $(this).find('form').on('submit', function(e){
                e.stopPropagation();
                e.preventDefault();
                $(this).closest('.pjax-container').load(imageUpdateUrl, $(this).serializeArray(), function(){
                    updatePanelContent(id);
                });

            });
        });
        useReplaceState = true;
    },

    'deleteImage': function(id){
        var imageData = imageUrls[id],
            imageDeleteUrl = imageData.deleteUrl;

        $('#image-update-container').load(imageDeleteUrl, null, function(){
            imagebaseRouter.prepGridForSidePanel();
            $(this).parent().removeClass('returned').addClass('flipped');

//            $(this).find('form').on('submit', function(e){
//                e.stopPropagation();
//                e.preventDefault();
//                // response could container JavaScript to remove representation
//            });
        });
        useReplaceState = true;
    },

    'viewImage': function(id){
        var imageData = imageUrls[id],
            imageContentUrl = imageData.contentUrl;
        imagebaseRouter.resetView();
        $('#image-detail-container').load(imageContentUrl, null, function(){
            imagebaseRouter.prepGridForSidePanel();
            updatePanelContent(id);
            $(this).parent().removeClass('flipped').addClass('returned');
        });
        useReplaceState = false;
    },

    'resetView': function(){
        $(document).off('closed');
        $('#modal').foundation('reveal', 'close');
        $('#image-detail-container').empty();
    },

    'prepGridForSidePanel': function(){
        $('#image-master-container').removeClass('medium-12').addClass('medium-8');
    }



});

function updatePanelContent(id){
    var $panelContainer = $('.image-panel[data-pk='+id+']');
    $panelContainer.load(imageUrls[id].panelUrl, null, function(){
        $panelContainer.addClass('updated');
        setTimeout(function(){
            $panelContainer.removeClass('updated');
        }, 1000);
    });
}


var imagebaseRouter = new ImagebaseRouter(),
    pageData = new PageData(),
    imageUrls;

$(function(){


    $('main').on('click', 'a[data-pjax]', function(e){
        e.preventDefault();
        e.stopPropagation();
        imagebaseRouter.navigate(e.currentTarget.pathname, {trigger: true, replace: useReplaceState});
    });

    pageData.fetch({
        success: function(model){
            imageUrls = model.get('images');
            if (window.location.pathname === '/'){
                history.replaceState(null, null, '/dashboard/');
            }
            Backbone.history.start({pushState: true, root:'/dashboard/'});
        },
        error: function(e){
        }
    });

});

