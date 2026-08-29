# main.py
import asyncio
import greenhouse_core.utils.processors as processors
import greenhouse_core.services.telemetry as telemetry


async def main():
    print("--- Старт сбора метрик ---")
    raw_results = await asyncio.gather(
        telemetry.fetch_sensor("TEMP_1"),
        telemetry.fetch_sensor("TEMP_2"),
        telemetry.fetch_sensor("TEMP_3")
    )

    print(f"Сырые данные с датчиков: {raw_results}")


    temperatures = [temp for sensor_id, temp in raw_results]
    print(f"Выделенные температуры: {temperatures}")

    final_history = processors.filter_and_boost_metrics(
        metrics=temperatures,
        min_threshold=25.0,
        history=metrics
    )

    print(f"--- Итоговая история (выращенная и отфильтрованная): {final_history} ---")

metrics = []

if __name__ == "__main__":
    asyncio.run(main())