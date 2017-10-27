<?php

use PHPUnit\Framework\TestCase;

putenv("PRE_BASE_DIR=" . realpath(__DIR__ . "/../"));

class MacroTest extends TestCase
{
    /**
     * @test
     * @dataProvider specs
     */
    public function can_transform_code($from, $expected)
    {
        Pre\Plugin\addMacro(__DIR__ . "/../source/macros.yay");

        $actual = Pre\plugin\format(Pre\Plugin\parse($this->format($from)));
        $this->assertEquals($this->format($expected), $actual);
    }

    private function format($code)
    {
        return "<?php\n\n" . trim($code) . "\n";
    }

    public static function specs()
    {
        $specs = [];

        $files = [
            __DIR__ . "/specs/async.spec",
        ];

        foreach ($files as $file) {
            $contents = file_get_contents($file);
            
            foreach (explode("---", $contents) as $spec) {
                array_push($specs, explode("~~~", $spec));
            }
        }

        return $specs;
    }
}
