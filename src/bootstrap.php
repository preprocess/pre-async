<?php

if (function_exists("\\Amp\\coroutine")) {
    Pre\addMacroPath(__DIR__ . "/macros-v1.pre");
} else {
    Pre\addMacroPath(__DIR__ . "/macros-v2.pre");
}
