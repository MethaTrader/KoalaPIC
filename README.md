
# KoalaPIC Web application for generating images from text

This project contains a web application for generating images from user-entered text. You can use this application to create graphic images for your social media, blogs, websites, and other projects.




![alt text](https://i.imgur.com/uVsnq6b.png)

# Setup

1) Docker Build
```bash
docker build -t koalapic . 
```

2) Run Docker
```bash
docker run -p 5000:80 koalapic
```

3) Go to http://localhost:5000/


### Docker compose
```bash
docker compose up
```

## API Reference

#### Image generation

```http
  GET /api/generate
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `prompt`  | `string` | **Required**. Your text    |


The result will be a URL link to the generated image.

To access the full information and functionality of the server go to
http://localhost:5000/docs

## Developers

- [@MethaTrader](https://www.github.com/MethaTrader)
- [@Moqu3f](https://github.com/Moqu3f)
- [@zetatul](https://github.com/zetatul)
- [@dezmond338](https://github.com/dezmond338)
- [@naumenkoanatoly](https://github.com/naumenkoanatoly)
