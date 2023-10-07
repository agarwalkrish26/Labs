<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $date_of_visit = $_POST["date_of_visit"];

    $to = $email; // Send email to the user
    $subject = "Appointment Confirmation - CHRIST (Deemed to be University)";
    $message = "Hello $name,\n\nYour appointment at CHRIST (Deemed to be University) Pune Lavasa Campus has been successfully booked for the date: $date_of_visit.\n\nThank you for choosing us. We look forward to your visit!\n\nBest Regards,\nCHRIST (Deemed to be University) Pune Lavasa Campus";
    $headers = "From: krish.agarwal@bds.christuniversity.in"; // Replace with your webmaster email or the university's official email

    if (mail($to, $subject, $message, $headers)) {
        echo "Appointment successfully booked! A confirmation email has been sent to $email.";
    } else {
        echo "Failed to send the email. Please try again.";
    }
}
?>