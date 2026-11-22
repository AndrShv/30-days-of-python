import click

@click.command()
@click.argument("sensor_id")
@click.option("-d", "--delay", default=1, help="Задержка опроса в секундах.")
@click.option("--verbose", is_flag=True, help="Включить детальный лог.")
def check_sensor(sensor_id: str, delay: int, verbose: bool):
    click.echo(f"Успешный запуск через Click!")
    click.echo(f"Датчик: {sensor_id} | Задержка: {delay} | Лог: {verbose}")

if __name__ == "__main__":
    check_sensor()