-- init.sql

-- Crear la tabla summary con los campos especificados
CREATE TABLE summary (
    id SERIAL PRIMARY KEY, -- Identificador único
    created_at TIMESTAMPTZ DEFAULT NOW(), -- Fecha de creación con zona horaria
    updated_at TIMESTAMPTZ DEFAULT NOW(), -- Fecha de actualización con zona horaria
    original_url VARCHAR(500) NOT NULL, -- URL original
    summary_text TEXT NOT NULL, -- Texto del resumen
    email VARCHAR(100), -- Correo electrónico (opcional)
    category VARCHAR(50) NOT NULL, -- Categoría de la noticia
    tone VARCHAR(50) NOT NULL, -- Tono de la noticia
    fake_news_level VARCHAR(50) DEFAULT 'Ninguno' -- Nivel de fake news
);