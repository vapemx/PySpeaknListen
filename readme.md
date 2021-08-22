# Py Speak and Listen

###### by: vapemx

### Description

Hi everyone! this is a little code wich you can use as a library in yout own python code.

This code have one function to talk and another one to listen. The functions uses your main input and output audio sources.

For now, you can find this code in English or Spanish. But you can push your own language:)

### Installation:

First of all you need to install two python libraries.

`pip install pyttsx3`
`pip install speech_rocognition`

After this, you can download the code from this GitHub page, or clone whole repository.

`git clone https://github.com/vapemx/PySpeaknListen.git`

Now, you can drag the file you need to use directly to your own project folder

- speak_n_listenES.py (spanish one)
- speak_n_listenEN.py (english one)

In your code (where you want to use this code), you need to import this one.

`import speak_n_listen-- as snl` (replace "--" for ES or EN)

### Usage:

At this step you can now use the functions!

`snl.speak()`

>With this one, the program speak the attribute that you give to it, can be a simple text or a variable.
    `snl.speak("Hello world")`
    or
    ```
    x = "Hellor world"
    snl.speak(x)
    ```

`snl.listen()`
>The program will listen to user, the result will be a text, you need to asisgante it to a variable
`x = snl.listen()`
Also, this function return a CLI answer, that prints, when the user can talk and if the program heard the input or not.

And that´s it, I´m here to listen suggestions, issues or whatever:)

Have a great day!
