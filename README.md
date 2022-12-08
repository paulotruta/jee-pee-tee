# jee-pee-tee

An Alexa Skill to interface with chat.openai.com. Ask a question and get answered with Alexa's soothing voice and GPT body of knowledge.

## Setup

1. Copy `config.example.json` to `config.json`
2. Get an OpenAI Session Token. Copy the cookie `__Secure-next-auth.session-token` from the `https://chat.openai.com` domain.
3. Add this token to the file `config.json` under `session_token`.
4. Zip this repository (to later import it in the Alexa Developer Console).
5. Create a new Alexa Skill in the Alexa Developer Console.
6. Go in the Code tab of the Alexa Developer Console and click "Import Code".
7. Select the zip file with the contents of this repository.
8. Click "Save" and "Build Model".
9. Go in the Test tab of the Alexa Developer Console and test! You can also use your alexa devices if they are connected to the same account!

## Usage

### Commands

- `Alexa, I want to ask jee pee tee a question`
- `Alexa, ask jee pee tee about our solar system`
- `Alexa, ask jee pee tee to explain the NP theorem`

# Disclaimer

This is not an official OpenAI product. This is a personal project and is not affiliated with OpenAI in any way.
