<?php
/**
 * Kontaktformular-Handler (statische Site, Mittwald-PHP).
 * VOR LIVEGANG PRÜFEN: mail()-Versand auf dem Mittwald-Tarif testen,
 * ggf. auf SMTP (PHPMailer) umstellen. Empfängeradresse unten kontrollieren.
 */
declare(strict_types=1);

$EMPFAENGER = 'info@schrott-berlin.de';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /kontakt/', true, 303);
    exit;
}

// Honeypot: Bots füllen das versteckte Feld "website" aus
if (!empty($_POST['website'] ?? '')) {
    header('Location: /danke/', true, 303); // Bot still abtropfen lassen
    exit;
}

$name    = trim(strip_tags($_POST['name'] ?? ''));
$email   = trim($_POST['email'] ?? '');
$subject = trim(strip_tags($_POST['subject'] ?? ''));
$message = trim(strip_tags($_POST['message'] ?? ''));
$privacy = isset($_POST['privacy']);

if ($name === '' || $message === '' || !$privacy
    || !filter_var($email, FILTER_VALIDATE_EMAIL)
    || mb_strlen($message) > 5000) {
    header('Location: /kontakt/?fehler=1', true, 303);
    exit;
}

$betreff = 'Kontaktformular schrott-berlin.de'
         . ($subject !== '' ? ': ' . mb_substr($subject, 0, 120) : '');
$body = "Name: {$name}\nE-Mail: {$email}\nBetreff: {$subject}\n\nNachricht:\n{$message}\n";
$headers = [
    'From'         => 'webformular@schrott-berlin.de',
    'Reply-To'     => $email,
    'Content-Type' => 'text/plain; charset=UTF-8',
];

mail($EMPFAENGER, $betreff, $body, $headers);

header('Location: /danke/', true, 303);
exit;
