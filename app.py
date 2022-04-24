import streamlit as st

from bbquote.lib import get_quote

"#These are the quotes with the show name"

quote = get_quote()  # assuming the function returns an author and a quote

f"{quote}"
