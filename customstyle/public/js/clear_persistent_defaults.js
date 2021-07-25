//check if logged out and set the my_session_default_settings=no
if (document.cookie.split(';').some((item) => item.includes('my_session_default_settings=yes' && 'system_user=no' && 'user_id=Guest'))) {
  document.cookie = "my_session_default_settings=no;SameSite=Lax";
  console.log("my_session_default_settings=no");
}
