<?php

namespace Pre\Async;

if (function_exists("\\Amp\\coroutine")) {
    define("PRE_ASYNC_WRAPPER", "\\Amp\\resolve");
} else {
    define("PRE_ASYNC_WRAPPER", "\\Amp\\call");
}
