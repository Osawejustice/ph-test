// Custom handler for WhatsApp form submission
(function($) {
    'use strict';
    
    $(document).ready(function() {
        // Override the Quform success handler for WhatsApp
        $('form.quform').on('quform-success', function(event, response) {
            if (response && response.whatsapp_link) {
                // Show success message
                console.log('Form submitted successfully. Redirecting to WhatsApp...');
                
                // Redirect to WhatsApp after a short delay
                setTimeout(function() {
                    window.location.href = response.whatsapp_link;
                }, 1500);
            }
        });
        
        // Alternative: Monitor the form submission directly
        var originalQuform = $.fn.Quform;
        $.fn.Quform = function(options) {
            var defaults = {
                success: function(response) {
                    // If response contains WhatsApp link, redirect
                    if (response && response.whatsapp_link) {
                        console.log('Redirecting to WhatsApp...');
                        setTimeout(function() {
                            window.location.href = response.whatsapp_link;
                        }, 2000);
                    }
                }
            };
            
            var settings = $.extend({}, defaults, options);
            return originalQuform.call(this, settings);
        };
    });
})(jQuery);
