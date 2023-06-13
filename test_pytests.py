import requests
import pytest


class TestCursos:
    headers = {'Authorization': 'Token ad500a96161f6de639976b8583627a144287032c'}
    base_url = 'http://localhost:8000/api/v2/cursos'

    def test_get_cursos(self):
        cursos = requests.get(url=f'{self.base_url}/', headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.base_url}/2/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            'titulo': 'Curso para testes',
            'url': 'http://www.linkedin.com.br'
        }

        result = requests.post(
            url=f'{self.base_url}/', headers=self.headers, data=novo)

        assert result.status_code == 201

    def test_put_curso(self):
        atualizado = {
            'titulo': 'Curso teste'
        }

        result = requests.patch(
            url=f'{self.base_url}/5/', headers=self.headers, data=atualizado)

        assert result.status_code == 200
