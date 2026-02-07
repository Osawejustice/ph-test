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
    
    // Prepare email
    $to = 'info@openheartshomecare.net';
    $email_subject = 'New Contact Form Submission - ' . $subject;
    
    $email_body = "You have received a new message from the contact form.\n\n";
    $email_body .= "Name: " . $name . "\n";
    $email_body .= "Email: " . $email . "\n";
    $email_body .= "Phone: " . $phone . "\n";
    $email_body .= "Subject: " . $subject . "\n";
    $email_body .= "Message:\n" . $message . "\n";
    
    // Send email
    $headers = "From: " . $email . "\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    
    $mail_sent = @mail($to, $email_subject, $email_body, $headers);
    
    if ($mail_sent) {
        $response = array(
            'type' => 'success',
            'message' => 'Thank you for contacting us! We will get back to you as soon as possible.'
        );
    } else {
        $response = array(
            'type' => 'error',
            'error' => 'There was an error sending your message. Please try again later.',
            'elementErrors' => array()
        );
    }
    
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
