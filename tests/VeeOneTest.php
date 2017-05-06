<?php

namespace Pre\Async;

use PHPUnit\Framework\TestCase;
use Pre\Testing\Spec;

class VeeOneTest extends TestCase
{
    public function testMacros()
    {
        \Pre\addMacroPath(__DIR__ . "/../src/macros-v1.pre");
        \Pre\removeMacroPath(__DIR__ . "/../src/macros-v2.pre");

        $spec = new Spec(__DIR__ . "/specs/async-vee-one.spec");

        try {
            $spec->run();
            $spec->clean();
        } catch (Exception $e) {
            $spec->dump();
            throw $e;
        }

        $this->assertNotEquals(Spec::BROKEN, $spec->status());
    }
}
