"""
CV Email Sender Script
Sends a combined Arabic + English email to recruitment companies
with CV attachment.
"""

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os

# ===== UPDATE THESE WITH YOUR CREDENTIALS =====
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'youssef.elsayed0111@gmail.com'   # Your Gmail
SENDER_PASSWORD = '<App Password>'                       # 16-character App Password
TEST_RECIPIENT = 'youssef.elsayed0555@gmail.com'

# ===== CV FILE PATH =====
CV_FILE_PATH = 'Youssef_Elsayed_CV.pdf'   # Put your CV PDF in the same folder as this script

# ===== EMAIL SUBJECT =====
EMAIL_SUBJECT = 'طلب توظيف – مطوّر برمجيات | Job Application – Software Engineer / Odoo Developer'

# ===== ALL RECIPIENT EMAILS =====
RECIPIENTS = [
    # شركة الملتقى (Almoltaqa)
    {'company': 'شركة الملتقى (Almoltaqa)',      'email': 'info@almoltaqa.com.eg'},
    {'company': 'شركة الملتقى (Almoltaqa)',      'email': 'eng@almoltaqa.com.eg'},
]


# ===== EMAIL BODY =====
def get_email_body():
    return """<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Job Application</title>
  <style>
    body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
    table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
    body { margin: 0 !important; padding: 0 !important; background-color: #f0f4f8; }

    @media only screen and (max-width: 620px) {
      .email-wrapper  { width: 100% !important; }
      .mobile-pad     { padding: 22px 18px !important; }
      .header-title   { font-size: 20px !important; }
      .header-sub     { font-size: 11px !important; }
      .badge          { display: inline-block !important; margin: 3px 2px !important; }
      .contact-label  { display: none !important; }
    }
  </style>
</head>
<body style="margin:0; padding:0; background-color:#f0f4f8;">

<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"
       style="background-color:#f0f4f8;">
  <tr>
    <td align="center" style="padding: 30px 12px;">

      <!-- ============================================ -->
      <!--                EMAIL CARD                    -->
      <!-- ============================================ -->
      <table role="presentation" class="email-wrapper" width="600" cellspacing="0"
             cellpadding="0" border="0"
             style="background-color:#ffffff; border-radius:14px; overflow:hidden;
                    box-shadow:0 6px 30px rgba(0,0,0,0.10);">

        <!-- ── HERO HEADER ── -->
        <tr>
          <td style="background:linear-gradient(135deg,#0f2c4e 0%,#1d55a0 55%,#3b82c4 100%);
                     padding:38px 40px 30px 40px;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
              <tr>
                <td width="68" valign="top" style="padding-right:18px;">
                  <table role="presentation" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style="width:64px; height:64px; border-radius:50%;
                                 background:rgba(255,255,255,0.15);
                                 border:2px solid rgba(255,255,255,0.45);
                                 text-align:center; vertical-align:middle;
                                 font-size:20px; font-weight:700; color:#ffffff;
                                 font-family:Arial,sans-serif; line-height:64px;">YE</td>
                    </tr>
                  </table>
                </td>
                <td valign="middle">
                  <div class="header-title"
                       style="font-size:24px; font-weight:700; color:#ffffff;
                              font-family:Arial,sans-serif; margin-bottom:7px;
                              letter-spacing:0.2px;">
                    Youssef El-Sayed Youssef
                  </div>
                  <div class="header-sub"
                       style="font-size:12.5px; color:rgba(255,255,255,0.82);
                              font-family:Arial,sans-serif; margin-bottom:6px;">
                    Software Engineer &nbsp;&middot;&nbsp; Odoo Developer &nbsp;&middot;&nbsp; Python Engineer
                  </div>
                  <div style="font-size:11.5px; color:rgba(255,255,255,0.60);
                              font-family:Arial,sans-serif;">
                    &#128205; Cairo, Egypt &mdash; Open to relocation &amp; remote work
                  </div>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- ── ENGLISH SECTION ── -->
        <tr>
          <td class="mobile-pad"
              style="padding:34px 40px 8px 40px; background-color:#ffffff;">

            <p style="margin:0 0 12px 0; font-size:15px; color:#1f2937;
                      font-family:Arial,sans-serif; line-height:1.6;">
              Dear Sir/Madam,
            </p>
            <p style="margin:0 0 26px 0; font-size:14.5px; color:#374151;
                      font-family:Arial,sans-serif; line-height:1.75;">
              I&rsquo;m reaching out to express my interest in
              <strong style="color:#0f2c4e;">Software Engineer / Odoo Developer</strong>
              opportunities through your agency. Please find my CV attached for your review.
            </p>

            <!-- Section heading -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="margin-bottom:4px;">
              <tr>
                <td style="padding-bottom:7px; border-bottom:2px solid #1d55a0;">
                  <span style="font-size:10.5px; font-weight:700; letter-spacing:2.2px;
                               color:#1d55a0; text-transform:uppercase;
                               font-family:Arial,sans-serif;">Key Highlights</span>
                </td>
              </tr>
            </table>

            <!-- Highlights rows -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="margin-bottom:26px;">
              <tr>
                <td style="padding:10px 0 10px 4px; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.55;">
                  <span style="color:#1d55a0; font-weight:700; margin-right:8px;">&#9656;</span>
                  Specialized in <strong>Odoo ERP</strong> development
                  <strong>(v14&ndash;v19)</strong> and multi-tenant SaaS platforms
                </td>
              </tr>
              <tr>
                <td style="padding:10px 0 10px 4px; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.55;">
                  <span style="color:#1d55a0; font-weight:700; margin-right:8px;">&#9656;</span>
                  Building a <strong>real-time GPS fleet telematics system</strong>
                  for a Saudi client (Galaxy Solutions ITC)
                </td>
              </tr>
              <tr>
                <td style="padding:10px 0 10px 4px; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.55;">
                  <span style="color:#1d55a0; font-weight:700; margin-right:8px;">&#9656;</span>
                  <strong>Software Instructor</strong> &mdash; Egypt&rsquo;s national
                  Digital Egypt Cubs Initiative
                </td>
              </tr>
              <tr>
                <td style="padding:10px 0 10px 4px; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.55;">
                  <span style="color:#1d55a0; font-weight:700; margin-right:8px;">&#9656;</span>
                  <strong>ICPC Competitor</strong> &mdash; ranked
                  <strong>5th out of 234 teams</strong> nationally
                </td>
              </tr>
              <tr>
                <td style="padding:10px 0 10px 4px;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.55;">
                  <span style="color:#1d55a0; font-weight:700; margin-right:8px;">&#9656;</span>
                  Solved <strong>2,000+ algorithmic problems</strong>
                  on Codeforces and other online judges
                </td>
              </tr>
            </table>

            <!-- Tech stack heading -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="margin-bottom:12px;">
              <tr>
                <td style="padding-bottom:7px; border-bottom:2px solid #1d55a0;">
                  <span style="font-size:10.5px; font-weight:700; letter-spacing:2.2px;
                               color:#1d55a0; text-transform:uppercase;
                               font-family:Arial,sans-serif;">Tech Stack</span>
                </td>
              </tr>
            </table>

            <!-- Badges -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="margin-bottom:34px;">
              <tr>
                <td style="font-family:Arial,sans-serif; line-height:2.4; padding-top:4px;">
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">Python</span>
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">Odoo ERP</span>
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">PostgreSQL</span>
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">REST APIs</span>
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">JavaScript</span>
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">C# .NET</span>
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">MQTT</span>
                  <span class="badge" style="display:inline-block;background:#eef2ff;color:#3730a3;
                    border:1px solid #c7d2fe;border-radius:20px;padding:4px 13px;
                    font-size:12px;font-weight:600;margin:2px 3px 2px 0;">IoT</span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- ── DIVIDER ── -->
        <tr>
          <td style="padding:0 40px;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0">
              <tr>
                <td style="border-top:1px solid #e5e7eb; width:40%;"></td>
                <td style="padding:0 14px; text-align:center; white-space:nowrap;
                           font-size:10.5px; color:#9ca3af; letter-spacing:1.8px;
                           text-transform:uppercase; font-family:Arial,sans-serif;">
                  النسخة العربية
                </td>
                <td style="border-top:1px solid #e5e7eb; width:40%;"></td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- ── ARABIC SECTION ── -->
        <tr>
          <td class="mobile-pad" dir="rtl"
              style="padding:28px 40px 8px 40px; background-color:#ffffff;
                     text-align:right;">

            <p style="margin:0 0 12px 0; font-size:15px; color:#1f2937;
                      font-family:Arial,sans-serif; line-height:1.7;">
              السلام عليكم ورحمة الله وبركاته،
            </p>
            <p style="margin:0 0 26px 0; font-size:14.5px; color:#374151;
                      font-family:Arial,sans-serif; line-height:1.8;">
              أتقدم إليكم بطلب توظيف في مجال
              <strong style="color:#0f2c4e;">تطوير البرمجيات وأنظمة ERP</strong>.
              يسعدني إرفاق سيرتي الذاتية للاطلاع.
            </p>

            <!-- Arabic section heading -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="margin-bottom:4px;">
              <tr>
                <td style="padding-bottom:7px; border-bottom:2px solid #1d55a0;">
                  <span style="font-size:10.5px; font-weight:700; letter-spacing:2px;
                               color:#1d55a0; font-family:Arial,sans-serif;">
                    خلاصة سريعة
                  </span>
                </td>
              </tr>
            </table>

            <!-- Arabic highlights -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="margin-bottom:26px;">
              <tr>
                <td style="padding:10px 4px 10px 0; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.6;">
                  <span style="color:#1d55a0; font-weight:700; margin-left:8px;">&#9666;</span>
                  خبرة في تطوير أنظمة <strong>Odoo ERP</strong>
                  (الإصدارات 14 حتى 19) وبناء منصات SaaS متعددة المستأجرين
                </td>
              </tr>
              <tr>
                <td style="padding:10px 4px 10px 0; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.6;">
                  <span style="color:#1d55a0; font-weight:700; margin-left:8px;">&#9666;</span>
                  بناء <strong>منظومة تتبع أسطول مركبات بـ GPS</strong>
                  في الوقت الفعلي لعميل سعودي (Galaxy Solutions ITC)
                </td>
              </tr>
              <tr>
                <td style="padding:10px 4px 10px 0; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.6;">
                  <span style="color:#1d55a0; font-weight:700; margin-left:8px;">&#9666;</span>
                  <strong>مدرّب برمجيات</strong> ضمن مبادرة مصر الرقمية الوطنية
                </td>
              </tr>
              <tr>
                <td style="padding:10px 4px 10px 0; border-bottom:1px solid #f3f4f6;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.6;">
                  <span style="color:#1d55a0; font-weight:700; margin-left:8px;">&#9666;</span>
                  مشارك في <strong>ICPC</strong> &mdash; المركز الـ
                  <strong>5 على مستوى مصر</strong> (من بين 234 فريق)
                </td>
              </tr>
              <tr>
                <td style="padding:10px 4px 10px 0;
                           font-family:Arial,sans-serif; font-size:13.5px;
                           color:#374151; line-height:1.6;">
                  <span style="color:#1d55a0; font-weight:700; margin-left:8px;">&#9666;</span>
                  حلّ أكثر من <strong>2,000 مسألة خوارزمية</strong>
                  على Codeforces ومنصات أخرى
                </td>
              </tr>
            </table>

            <p style="margin:0 0 32px 0; font-size:13.5px; color:#6b7280;
                      font-family:Arial,sans-serif; line-height:1.75;">
              أتطلع إلى الانضمام لفرصة مناسبة، وأنا متاح للتواصل في أي وقت.
            </p>
          </td>
        </tr>

        <!-- ── CONTACT FOOTER ── -->
        <tr>
          <td style="background-color:#f8fafc; border-top:1px solid #e5e7eb;
                     padding:28px 40px 30px 40px; border-radius:0 0 14px 14px;">

            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="margin-bottom:18px;">
              <tr>
                <td style="padding-bottom:7px; border-bottom:2px solid #1d55a0;">
                  <span style="font-size:10.5px; font-weight:700; letter-spacing:2.2px;
                               color:#1d55a0; text-transform:uppercase;
                               font-family:Arial,sans-serif;">Portfolio &amp; Contact</span>
                </td>
              </tr>
            </table>

            <!-- Contact table with alternating rows -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0"
                   style="border-radius:8px; overflow:hidden; margin-bottom:26px;">

              <tr>
                <td width="110" style="padding:9px 12px; background:#eef2ff;
                           vertical-align:middle; font-family:Arial,sans-serif;
                           font-size:12.5px; color:#4b5563; font-weight:700;
                           border-radius:6px 0 0 0;">
                  &#127760; Portfolio
                </td>
                <td style="padding:9px 14px; background:#eef2ff; vertical-align:middle;
                           font-family:Arial,sans-serif; font-size:13px;
                           border-radius:0 6px 0 0;">
                  <a href="https://youssef22222.github.io"
                     style="color:#1d55a0; text-decoration:none; font-weight:600;">
                    youssef22222.github.io
                  </a>
                </td>
              </tr>

              <tr>
                <td style="padding:9px 12px; background:#ffffff; vertical-align:middle;
                           font-family:Arial,sans-serif; font-size:12.5px;
                           color:#4b5563; font-weight:700; border-bottom:1px solid #f3f4f6;">
                  &#128231; Email
                </td>
                <td style="padding:9px 14px; background:#ffffff; vertical-align:middle;
                           font-family:Arial,sans-serif; font-size:13px;
                           border-bottom:1px solid #f3f4f6;">
                  <a href="mailto:youssef.elsayed0111@gmail.com"
                     style="color:#1d55a0; text-decoration:none;">
                    youssef.elsayed0111@gmail.com
                  </a>
                </td>
              </tr>

              <tr>
                <td style="padding:9px 12px; background:#eef2ff; vertical-align:middle;
                           font-family:Arial,sans-serif; font-size:12.5px;
                           color:#4b5563; font-weight:700;">
                  &#128222; Phone
                </td>
                <td style="padding:9px 14px; background:#eef2ff; vertical-align:middle;
                           font-family:Arial,sans-serif; font-size:13px; color:#374151;">
                  +201113885845 &nbsp;/&nbsp; +201013797110
                </td>
              </tr>

              <tr>
                <td style="padding:9px 12px; background:#ffffff; vertical-align:middle;
                           font-family:Arial,sans-serif; font-size:12.5px;
                           color:#4b5563; font-weight:700;
                           border-radius:0 0 0 6px;">
                  &#128279; LinkedIn
                </td>
                <td style="padding:9px 14px; background:#ffffff; vertical-align:middle;
                           font-family:Arial,sans-serif; font-size:13px;
                           border-radius:0 0 6px 0;">
                  <a href="https://linkedin.com/in/YoussefElsayedYoussef"
                     style="color:#1d55a0; text-decoration:none;">
                    linkedin.com/in/YoussefElsayedYoussef
                  </a>
                </td>
              </tr>

            </table>

            <p style="margin:0; text-align:center; font-size:12.5px; color:#9ca3af;
                      font-family:Arial,sans-serif; line-height:1.6;">
              شكراً لاهتمامكم &nbsp;|&nbsp; Thank you for your time and consideration.
            </p>

          </td>
        </tr>

      </table>
      <!-- END EMAIL CARD -->

    </td>
  </tr>
</table>

</body>
</html>"""


def build_message(recipient_email):
    """Build the email message with CV attachment"""
    message = MIMEMultipart('mixed')
    message['From'] = SENDER_EMAIL
    message['To'] = recipient_email
    message['Subject'] = EMAIL_SUBJECT

    # Attach HTML body
    html_part = MIMEText(get_email_body(), 'html', 'utf-8')
    message.attach(html_part)

    # Attach CV PDF if file exists
    if os.path.exists(CV_FILE_PATH):
        with open(CV_FILE_PATH, 'rb') as f:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(f.read())
            encoders.encode_base64(attachment)
            attachment.add_header(
                'Content-Disposition',
                f'attachment; filename="Youssef_ElSayed_CV.pdf"'
            )
            message.attach(attachment)
    else:
        print(f"  ⚠️  CV file not found at '{CV_FILE_PATH}' — sending without attachment")

    return message


# ===================================================
#  TEST SMTP CONNECTION
# ===================================================

def test_smtp_connection():
    """Test SMTP connection and authentication"""
    print("=" * 50)
    print("SMTP Connection Test")
    print("=" * 50)

    print("\n[1/4] Testing connection to SMTP server...")
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
        print("✓ Successfully connected to SMTP server")
    except Exception as e:
        print(f"✗ Failed to connect: {e}")
        return False

    print("\n[2/4] Testing TLS encryption...")
    try:
        server.starttls()
        print("✓ TLS encryption enabled")
    except Exception as e:
        print(f"✗ Failed to enable TLS: {e}")
        server.quit()
        return False

    print("\n[3/4] Testing authentication...")
    try:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("✓ Authentication successful")
    except smtplib.SMTPAuthenticationError as e:
        print(f"✗ Authentication failed: {e}")
        print("\nPossible reasons:")
        print("  - Wrong email or password")
        print("  - Using regular password instead of App Password")
        print("  - App Password not enabled")
        print("  - 2-Step Verification not enabled")
        server.quit()
        return False
    except Exception as e:
        print(f"✗ Login error: {e}")
        server.quit()
        return False

    print("\n[4/4] Sending test email...")
    try:
        message = build_message(TEST_RECIPIENT)
        message.replace_header('Subject', '[TEST] ' + EMAIL_SUBJECT)
        server.send_message(message)
        print(f"✓ Test email sent successfully to {TEST_RECIPIENT}")
    except Exception as e:
        print(f"✗ Failed to send test email: {e}")
        server.quit()
        return False

    server.quit()
    print("\n" + "=" * 50)
    print("✓ ALL TESTS PASSED!")
    print("=" * 50)
    return True


def check_app_password_format():
    """Check if App Password is in correct format"""
    print("\n" + "=" * 50)
    print("App Password Format Check")
    print("=" * 50)
    clean_password = SENDER_PASSWORD.replace(' ', '')
    print(f"\nPassword length: {len(clean_password)} characters (expected: 16)")
    if len(clean_password) == 16:
        print("✓ Password length is correct")
        return True
    else:
        print("✗ Password length is incorrect — App Password must be exactly 16 characters")
        return False


# ===================================================
#  MAIN SEND FUNCTION
# ===================================================

def send_all_emails():
    """Send CV email to all recruitment companies"""
    print("\n" + "=" * 60)
    print("       CV EMAIL SENDER — Starting...")
    print("=" * 60)
    print(f"Total recipients: {len(RECIPIENTS)}")
    print(f"CV file: {'✓ Found' if os.path.exists(CV_FILE_PATH) else '✗ NOT FOUND — will send without attachment'}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    success_list = []
    failed_list = []

    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("\n✓ Logged in successfully. Sending emails...\n")
    except Exception as e:
        print(f"\n✗ Could not connect/login: {e}")
        return

    for i, recipient in enumerate(RECIPIENTS, 1):
        company = recipient['company']
        email = recipient['email']
        print(f"[{i:02d}/{len(RECIPIENTS)}] Sending to {company} <{email}> ...", end=' ')

        try:
            msg = build_message(email)
            server.send_message(msg)
            print("✓ Sent")
            success_list.append({'company': company, 'email': email})
        except Exception as e:
            print(f"✗ Failed: {e}")
            failed_list.append({'company': company, 'email': email, 'error': str(e)})

        # Wait 3 seconds between emails to avoid spam filters
        if i < len(RECIPIENTS):
            time.sleep(3)

    server.quit()

    # ===== SUMMARY =====
    print("\n" + "=" * 60)
    print("                    SUMMARY")
    print("=" * 60)
    print(f"✓ Successfully sent : {len(success_list)}")
    print(f"✗ Failed            : {len(failed_list)}")

    if failed_list:
        print("\nFailed recipients:")
        for f in failed_list:
            print(f"  - {f['company']} <{f['email']}> → {f['error']}")

    print(f"\nFinished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


# ===================================================
#  ENTRY POINT
# ===================================================

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("         CV EMAIL SENDER")
    print("=" * 60)
    print(f"  Sender     : {SENDER_EMAIL}")
    print(f"  SMTP Host  : {SMTP_HOST}:{SMTP_PORT}")
    print(f"  Recipients : {len(RECIPIENTS)} emails")
    print(f"  CV File    : {CV_FILE_PATH}")

    # Step 1: Check password format
    if not check_app_password_format():
        print("\n⚠️  Fix your App Password before running!")
        exit(1)

    # Step 2: Test SMTP + send test email
    print("\n" + "=" * 60)
    print("STEP 1 — Run connection test first? (sends test email to yourself)")
    choice = input("Enter 't' to test first, or 's' to skip and send directly: ").strip().lower()

    if choice == 't':
        if not test_smtp_connection():
            print("\n✗ Fix SMTP issues before sending to all companies.")
            exit(1)
        print("\n✓ Test passed! Check your inbox before continuing.")
        input("\nPress ENTER to start sending to all companies...")

    # Step 3: Send to all companies
    send_all_emails()

"""
SETUP INSTRUCTIONS:
==================
1. Place this script in the same folder as your CV PDF file
2. Rename your CV to match CV_FILE_PATH above (or update the path)
3. Update SENDER_PASSWORD with your 16-char Gmail App Password:
   - Enable 2-Step Verification: https://myaccount.google.com/security
   - Generate App Password: https://myaccount.google.com/apppasswords
   - Select "Mail" + "Windows Computer" → copy the 16-char password
4. Run: python send_cv_emails.py
5. Choose 't' to test first (recommended), then 's' to send all

TROUBLESHOOTING:
================
- Auth error  → Use App Password, not your regular Gmail password
- Timeout     → Check firewall / port 587
- No attachment → Make sure CV PDF is in the same folder and name matches
"""
