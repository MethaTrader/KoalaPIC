const express = require('express');
const axios = require('axios');
const app = express();
const { Configuration, OpenAIApi } = require('openai');

const configuration = new Configuration({
    apiKey: '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',
});
const openai = new OpenAIApi(configuration);

app.use(express.json()); // Добавьте поддержку JSON для входящих запросов
app.use(express.static(__dirname + '/'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/api/generate', async (req, res) => {
    const { prompt, size } = req.body;

    const imageSize =
        size === 'small' ? '256x256' : size === 'medium' ? '512x512' : '1024x1024';

    try {
        const response = await openai.createImage({
            prompt,
            n: 1,
            size: imageSize,
        });

        const imageUrl = response.data.data[0].url;

        res.status(200).json({
            success: true,
            data: imageUrl,
        });
    } catch (error) {
        if (error.response) {
            console.log(error.response.status);
            console.log(error.response.data);
        } else {
            console.log(error.message);
        }

        res.status(400).json({
            success: false,
            error: 'The image could not be generated',
        });
    }
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
