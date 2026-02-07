<?php
header('Content-Type: application/json');

// Check if this is an AJAX request
if (isset($_POST['quform_ajax'])) {
    // Validate required fields
    $required_fields = array('name', 'email', 'subject', 'message');
    $errors = array();
    $element_errors = array();
    
    foreach ($required_fields as $field) {
        if (empty($_POST[$field])) {
            $element_errors[$field] = array('This field is required');
            $errors[] = ucfirst($field) . ' is required';
        }
    }
    
    // Validate email format
    if (!empty($_POST['email']) && !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
        $element_errors['email'] = array('Please enter a valid email');
        $errors[] = 'Please enter a valid email';
    }
    
    if (!empty($errors)) {
        $response = array(
            'type' => 'error',
            'error' => 'Please correct the following errors: ' . implode(', ', $errors),
            'elementErrors' => $element_errors
        );
        echo json_encode($response);
        exit;
    }
    
    // Get form data
    $name = sanitize_input($_POST['name']);
    $email = sanitize_input($_POST['email']);
    $subject = sanitize_input($_POST['subject']);
    $phone = isset($_POST['phone']) ? sanitize_input($_POST['phone']) : '';
    $message = sanitize_input($_POST['message']);
    
    // Prepare WhatsApp message
    // WhatsApp phone number (with country code, no special characters)
    $whatsapp_phone = '17785819636'; // 1-778-581-9636
    
    // Create formatted message for WhatsApp
    $whatsapp_message = "Name: " . $name . "\n";
    $whatsapp_message .= "Email: " . $email . "\n";
    if (!empty($phone)) {
        $whatsapp_message .= "Phone: " . $phone . "\n";
    }
    $whatsapp_message .= "Subject: " . $subject . "\n\n";
    $whatsapp_message .= "Message:\n" . $message;
    
    // URL encode the message
    $encoded_message = urlencode($whatsapp_message);
    
    // Generate WhatsApp link
    $whatsapp_link = "https://api.whatsapp.com/send?phone=" . $whatsapp_phone . "&text=" . $encoded_message;
    
    // Return success with WhatsApp link
    $response = array(
        'type' => 'success',
        'message' => 'Thank you for contacting us! Redirecting to WhatsApp...',
        'whatsapp_link' => $whatsapp_link
    );
    
    echo json_encode($response);
    exit;
} else {
    echo json_encode(array(
        'type' => 'error',
        'error' => 'Invalid request',
        'elementErrors' => array()
    ));
    exit;
}

function sanitize_input($input) {
    $input = trim($input);
    $input = stripslashes($input);
    $input = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
    return $input;
}
?>
