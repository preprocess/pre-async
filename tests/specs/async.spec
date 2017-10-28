interface AsyncInterface
{
    async public function run();
}

~~~

interface AsyncInterface
{
    public function run(): \Amp\Promise;
}

---

class AsyncClass
{
    async public function first(array $data = [])
    {
        await \Amp\File\get("path/to/file");
    }

    async public function second()
    {
        return "boo!";
    }

    async public static function complex(): string
    {

    }
}

~~~

class AsyncClass
{
    public function first(array $data = []): \Amp\Promise
    {
        return \Amp\call(function () {
            yield \Amp\File\get("path/to/file");
        });
    }

    public function second(): \Amp\Promise
    {
        return \Amp\call(function () {
            return "boo!";
            yield;
        });
    }

    public static function complex(): \Amp\Promise
    {
        return \Amp\call(function () {
            yield;
        });
    }
}

---

$first = async function() {
    yield "here";
};

$second = async function() {
    $this->something();
    yield $thing;
};

$third = async () => {
    yield $thing;
};

~~~

$first = function (): \Amp\Promise {
    return \Amp\call(function () {
        yield "here";
    });
};

$second = [$thing = $thing ?? null, "fn" => function () use (&$thing): \Amp\Promise {
    return \Amp\call(function () use (&$thing) {
        $this->something();
        yield $thing;
    });
}]["fn"];

$third = [$thing = $thing ?? null, "fn" => function () use (&$thing): \Amp\Promise {
    return \Amp\call(function () use (&$thing) {
        yield $thing;
    });
}]["fn"];
