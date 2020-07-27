import lib.local_debug as local_debug
from configuration import configuration

if local_debug.is_debug():
    pass
elif configuration.get_mode() == configuration.WS2801:
    from renderers import ws2801
elif configuration.get_mode() == configuration.WS281x:
    from renderers import ws281x
else:
    from renderers import led, led_pwm


def get_renderer(
    airport_render_config: dict
):
    """
    Returns the renderer to use based on the type of
    LED lights given in the config.

    Returns:
        renderer -- Object that takes the colors and airport config and
        sets the LEDs.
    """

    if local_debug.is_debug():
        return None

    if configuration.get_mode() == configuration.WS2801:
        pixel_count = configuration.CONFIG[configuration.PIXEL_COUNT_KEY]
        spi_port = configuration.CONFIG[configuration.SPI_PORT_KEY]
        spi_device = configuration.CONFIG[configuration.SPI_DEVICE_KEY]

        return ws2801.Ws2801Renderer(pixel_count, spi_port, spi_device)
    elif configuration.get_mode() == configuration.WS281x:
        pixel_count = configuration.CONFIG[configuration.PIXEL_COUNT_KEY]
        gpio_pin = configuration.CONFIG[configuration.GPIO_PIN_KEY]

        return ws281x.Ws281xRenderer(pixel_count, gpio_pin)
    elif configuration.get_mode() == configuration.PWM:
        return led_pwm.LedPwmRenderer(airport_render_config)
    else:
        # "Normal" LEDs
        return led.LedRenderer(airport_render_config)