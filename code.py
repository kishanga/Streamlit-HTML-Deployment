import streamlit as st
import streamlit.components.v1 as components

# Specify html code below
components.html(
    """
    <h1> My Portfolio </h1>
    <div> I am a junior data scientist specialising in Python and Machine Learning.</div>
    <hr />
    <div> Project 1 - <a href="http://www.github.com" target="_blank">GitHub Link</a> </div>
    <div> Project 2 - <a href="http://www.github.com" target="_blank">GitHub Link</a> </div>
    """,
    height=600,
)